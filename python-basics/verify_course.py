"""Validate the Python Basics source tree against InterCourses and run lesson checks.

Run: python python-courses/python-basics/verify_course.py
Requires the sibling intercourses backend and its Python dependencies.
"""
from __future__ import annotations

import ast
import contextlib
import io
import os
import re
import sys
import tempfile
from collections import Counter
from pathlib import Path

COURSE = Path(__file__).resolve().parent
WORKSPACE = COURSE.parents[1]
sys.path.insert(0, str(WORKSPACE / "intercourses/backend/src"))
from app.content.loader import ContentLoader, split_front_matter  # noqa: E402


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run_source(files: dict[str, str], *, name: str) -> str:
    with tempfile.TemporaryDirectory() as temp, contextlib.redirect_stdout(io.StringIO()) as stdout:
        root = Path(temp)
        for filename, source in files.items():
            path = root / filename
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(source)
        previous = os.getcwd()
        previous_path = sys.path[:]
        sys.path.insert(0, temp)
        try:
            os.chdir(temp)
            exec(compile(files["main.py"], name, "exec"), {"__name__": "__main__", "__file__": str(root / "main.py")})
        finally:
            os.chdir(previous)
            sys.path[:] = previous_path
            for key in list(sys.modules):
                if key in {Path(p).stem for p in files if p != "main.py"}:
                    del sys.modules[key]
        return stdout.getvalue().strip()


def run_python_tests(lesson_dir: Path, files: dict[str, str]) -> tuple[int, list[str]]:
    path = lesson_dir / "test_main.py"
    if not path.is_file():
        return 0, []
    text = path.read_text()
    tree = ast.parse(text, filename=str(path))
    names = [node.name for node in tree.body if isinstance(node, ast.FunctionDef) and node.name.startswith("test_")]
    check(bool(names), f"No Python tests in {path}")
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        for filename, source in files.items():
            destination = root / ("solution.py" if filename == "main.py" else filename)
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(source)
        prior_path = sys.path[:]
        prior_module = sys.modules.pop("solution", None)
        sys.path.insert(0, temp)
        previous = os.getcwd()
        os.chdir(temp)
        failed = []
        try:
            namespace: dict[str, object] = {}
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    exec(compile(text, str(path), "exec"), namespace)
            except Exception as exc:
                return len(names), [f"module import: {exc}"]
            for name in names:
                try:
                    with contextlib.redirect_stdout(io.StringIO()):
                        namespace[name]()
                except Exception as exc:
                    failed.append(f"{name}: {exc}")
        finally:
            os.chdir(previous)
            sys.path[:] = prior_path
            sys.modules.pop("solution", None)
            if prior_module is not None:
                sys.modules["solution"] = prior_module
            for key in {Path(p).stem for p in files if p != "main.py"}:
                sys.modules.pop(key, None)
        return len(names), failed


def main() -> None:
    loader = ContentLoader(COURSE.parent)
    courses = [course for course in loader.load_courses() if course.slug == "python-basics"]
    check(len(courses) == 1, "course not discovered")
    course = courses[0]
    meta, _ = split_front_matter((COURSE / "course.md").read_text())
    expected = [entry["slug"] for entry in meta["modules"]]
    check(len(expected) >= 10, "source topics are compressed into too few modules")
    check([module.slug for module in course.modules] == expected, "module order/discovery differs from manifest")
    counts: Counter[str] = Counter()
    tasks = 0
    runnable = 0
    for module in course.modules:
        check(module.lessons, f"empty module {module.slug}")
        check(module.quiz is not None and len(module.quiz.questions) >= 2, f"missing quiz in {module.slug}")
        check([lesson.sort_order for lesson in module.lessons] == list(range(1, len(module.lessons) + 1)), f"lesson order in {module.slug}")
        module_counts = Counter(lesson.lesson_type for lesson in module.lessons)
        if module.slug != "next-steps":
            check(module_counts["coding"] >= module_counts["interactive"] + module_counts["informational"], f"not practice-led: {module.slug}")
            check(any(lesson.slug.startswith("exercise-") for lesson in module.lessons), f"no explicit exercise in {module.slug}")
        counts.update(module_counts)
        for lesson in module.lessons:
            path = COURSE.parent / lesson.content_path
            directory = path.parent
            front, body = split_front_matter(path.read_text())
            for key in ("summary", "seo_title", "seo_description", "seo_keywords"):
                check(bool(front.get(key)), f"missing {key}: {path}")
            check(lesson.language == "python" and lesson.runtime == "pyodide", f"wrong runtime: {path}")
            check(lesson.lesson_type in {"coding", "interactive", "informational"}, f"wrong lesson type: {path}")
            for asset in re.findall(r"!\[[^]]+\]\(([^)\s]+)", body):
                check((directory / asset).is_file(), f"missing image: {directory / asset}")
            if lesson.lesson_type == "interactive":
                blocks = re.findall(r"```python run\n(.*?)\n```", body, re.S)
                check(len(blocks) == len(lesson.interactive_tests) > 0, f"block mismatch: {path}")
                for index, (code, expected_block) in enumerate(zip(blocks, lesson.interactive_tests)):
                    check(expected_block.index == index, f"block index: {path}")
                    actual = run_source({"main.py": code}, name=f"{lesson.slug}-{index}")
                    check(actual == expected_block.expected_output.strip(), f"block output: {path}: {actual!r}")
                    runnable += 1
            if lesson.lesson_type == "coding":
                starter = {part.path: part.content for part in lesson.code_files}
                answer = {part.path: part.content for part in lesson.solution_code_files}
                check("main.py" in starter and "main.py" in answer, f"missing main.py: {path}")
                check(starter.keys() == answer.keys(), f"solution/supporting files differ: {path}")
                for filename, source in starter.items():
                    ast.parse(source, filename=str(directory / filename))
                for filename, source in answer.items():
                    ast.parse(source, filename=str(directory / "solution" / filename))
                numbered = re.findall(r"^\d+\.\s", body, re.M)
                js_count = len(re.findall(r"^test\(", lesson.test_code or "", re.M))
                py_count, failures = run_python_tests(directory, answer)
                check(not failures, f"solution fails {path}: {failures}")
                check(len(numbered) == js_count + py_count > 0, f"task/test mismatch: {path} ({len(numbered)} tasks, {js_count} JS, {py_count} Python)")
                _, starter_failures = run_python_tests(directory, starter)
                if py_count:
                    check(len(starter_failures) == py_count, f"starter already passes checks: {path}: {starter_failures}")
                output = run_source(answer, name=str(path))
                initial = run_source(starter, name=str(path) + ":starter")
                if js_count:
                    check(output != initial, f"JS output test has no visible starter difference: {path}")
                check("Run" in body and "Submit" in body, f"missing practice instructions: {path}")
                tasks += len(numbered)
                print(f"  {module.slug}/{lesson.slug}: {len(numbered)} tasks; answer output {output!r}")
    print(f"PASS: {len(course.modules)} modules, {sum(counts.values())} lessons ({dict(counts)}), {tasks} coding tasks, {runnable} runnable examples, {len(course.modules)} quizzes")


if __name__ == "__main__":
    main()
