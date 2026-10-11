---
title: Import NumPy as np
slug: setup-and-import
order: 2
language: python
lesson_type: interactive
runtime: pyodide
pyodide_packages:
  - numpy
summary: Import NumPy as np, run a short example, and learn the optional local installation
  command.
seo_title: Import NumPy as np | NumPy for beginners
seo_description: Import NumPy as np, run a short example, and learn the optional local
  installation command.
seo_keywords:
  - NumPy
  - Python arrays
  - setup and import
---

The course examples are ready to use NumPy. You don't need to install anything to run them here.

Start a NumPy program with `import numpy as np`. The `as np` part gives the library a short name. When you write `np.array(...)`, you're asking NumPy to create an array.

```python run
import numpy as np
print(np.array([8, 13]).tolist())
```

Press **Run** and look for `[8, 13]`. Each example includes its own import because the blocks run independently.

In the following lesson, `main.py` will be editable. **Run** shows what your program does; **Submit** checks the requested change. The import is supplied there, so you can focus on the array.

## Optional: use NumPy on your computer

If you're staying in the course editor, skip this section.

If Python is already installed on your computer, open a terminal in a practice folder and create a **virtual environment**. This is a separate folder for the project's Python packages; it keeps them apart from packages used by other projects.

On Windows, run these commands one at a time:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install numpy
.\.venv\Scripts\python.exe -c "import numpy as np; print(np.array([8, 13]))"
```

On macOS or Linux:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install numpy
.venv/bin/python -c "import numpy as np; print(np.array([8, 13]))"
```

These commands use the environment's Python directly, so you don't need to activate it. The final command should print `[ 8 13]`; spacing can differ from Python's list display. Use that same environment's Python when you run a saved `.py` file.

If `venv` isn't available on Linux, install your distribution's Python virtual-environment package first. Local setup is optional; it doesn't affect the course checks.
