# Curriculum design and source coverage

The original topic outline is preserved in `source-outline.md`. The exact ordered inventory is in `curriculum-plan.json`. These files are maintainer material, not extra learner lessons.

## Audience and lesson contract

Learners know basic Python functions, collections, loops, imports, and basic exception handling. Classes start from zero. Every published lesson is a coding exercise with an incomplete editable `main.py`, hidden `test_main.py`, and a complete `solution/main.py`. Syntax and reasoning belong in the instruction pane. Short examples use different data from the exercise; the learner still writes the assessed behavior.

Each numbered task corresponds to one synchronous test function. Supplied code and already-completed project behavior are setup, not graded tasks. Hints are only useful in the context of an actual task. No reading-only or passive runnable demonstrations count toward the lesson target.

## Source-to-module coverage

| Original outline | Expanded location | Design decision |
| --- | --- | --- |
| Classes, objects, class attributes, data attributes, methods, initialization, class scope | 01 Classes and objects | Separate shared defaults, instance shadowing, and independent mutable state. |
| Function attributes, classes being callable, properties, read-only/computed properties, static methods | 02 Object interfaces | Include bound methods and class factories to distinguish function, method, class, and instance calls. Teach decorator syntax before relying on it. |
| String representations, operators, comparisons, length, truth, hashing, callable objects, formatting, finalization | 03 Python protocols | Arithmetic operations have separate exercises. Equality and hashing are coupled deliberately. Finalization is not treated as reliable resource management. |
| Single inheritance, object, extension, overriding, super, slots, multiple inheritance, diamond, MRO | 04 Inheritance and composition | Move before the animal hierarchy project. Add composition as an alternative to inheritance. |
| Animal, Bird, Fish hierarchy | 05 Animal rescue project | Build a register and care report through cumulative stages. |
| Account, SavingsAccount, CurrentAccount, FixedDeposit, InterestCalculator | 06 Banking project | Keep interest calculation usable independently. State simplified integer-money rules explicitly. |
| Enums, custom/explicit/automatic values, membership, uniqueness, methods, iteration, dataclass, bool, isinstance | 07 Enums and records | Interpret the ambiguous dataclass item as enums in records and dataclass values inside enums; do not decorate an Enum directly as a dataclass. |
| Descriptor get/set/delete/set_name, lookup, property/function connections | 08 Descriptors | Separate class access, per-instance storage, and data versus non-data lookup priority. |
| Python errors, handling, custom errors | 09 Errors and contracts | Add exception details, chaining, cleanup, and optional abstract contracts after concrete inheritance experience. |
| Ecommerce CLI with product/cart/order/invoice workflows | 10 Console shop project | Use deterministic scripted console commands through main.py, not a blocking input prompt or network service. |

## Project continuity

Project lessons must carry the previous reference implementation into the next starter, except for an explicitly explained refactor. Each stage adds one focused responsibility. Tests for the current task use fresh fixtures and varied values rather than relying on the demonstration printout. The final shop is an in-memory educational application; no payment processing, durable database, or external service is implied.

## Verification boundaries

Native Python checks establish syntax and behavior in that interpreter. Browser worker checks establish compatibility with the application's Python runner and Submit callback. Neither alone establishes full application editor, navigation, quiz interaction, or responsive-layout acceptance. The final verification report records which checks actually ran, their source inventory, and any remaining gaps.

The sibling authoring repository is the canonical source for this task. InterCourses can preview it using `CONTENT_DIR` pointed at the parent `python-courses` directory. Publication through the application's separately checked-out content submodule and stable progress catalog is a separate release step; no gitlink, deployment, or historical progress identifier should change silently during lesson authoring.
