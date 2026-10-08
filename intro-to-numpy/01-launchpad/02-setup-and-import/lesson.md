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


Press **Run** on the example below. Next, open the editor in the following lesson, write `import numpy as np`, press **Run** to inspect your output, and **Submit** to check your work. Every runnable block includes its own import because each example stands alone.

```python run
import numpy as np
print(np.array([8, 13]).tolist())
```

To work on your personal computer instead, activate your Python environment and run `python -m pip install numpy` in a terminal. Then import NumPy in your `.py` file. You do not need that installation step to complete these lessons.
