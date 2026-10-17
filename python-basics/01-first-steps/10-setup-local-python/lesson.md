---
title: "Set up Python Locally"
slug: setup-local-python
order: 10
language: python
lesson_type: informational
summary: Install Python on your computer and run your first saved script, or keep learning in the browser.
seo_title: "Install Python on Windows, macOS or Linux | Python Basics"
seo_description: Follow Windows installation steps or use a macOS or Linux package manager, then save and run a first Python file. Local setup is optional.
seo_keywords: [install python windows, python mac homebrew, python linux setup, run python script]
---

# Run Python on your own computer (optional)

You've already run Python code in the course. If you want to experiment with Python code on your system or want to build a local software, you might need to write code in your own system.

If you want to install Python on your system, you will have to follow instructions for one of the following based on your operating system.

| Your computer | Installation route |
| --- | --- |
| Windows | Python Install Manager, followed by a Python runtime |
| macOS | Homebrew, a tool that installs software from your terminal |
| Linux | Your distribution's package manager: `apt` or `dnf` |

A **terminal** is an application where you type commands for your computer. You can run below installation commands from the terminal application in your system. 

## Windows: install Python

### 1. Get the official installer

Open the official Python downloads page in your browser:

`https://www.python.org/downloads/`

Choose the Python version you want to install for Windows system and it will download a installation file. Open the downloaded installer and select **Install** and follow the software installation prompts.

### 2. Check your installation

Once you've finished installation, you can start a Powershell session and run below commands to verify your installation.

```powershell
python --version
```

You should see a version beginning with `Python 3`. 

```powershell
python -c "print('Hello from the Space camp')"
```

The `-c` option runs the Python code inside the quotes. Look for `Hello from the Space camp` on its own line.

## macOS: install with Homebrew

Newer versions of Mac have Python installed so you can check directly in your Terminal app with the verification step.

### 1. Open Terminal and check

Open Terminal app and run below command.

```bash
python3 --version
```

If you get an error saying `command not found`, you can install Python using homebrew as mentioned in the next step. You may need to install Homebrew.

### 2. Install Python

```bash
brew install python
```

This command installs Python in your system.

### 3. Run a small program

```bash
python3 --version
```

```bash
python3 -c "print('Hello from the Space Camp')"
```

You should see the output of the above command in the terminal.

## Linux: use your distribution's package manager

Many Linux distributions include Python 3 for system tools. Open your terminal and check:

```bash
python3 --version
```

If Python is missing, use specific package manager for your Linux distro; i.e. `apt` for Ubuntu, `yum` for CentOS, etc.

### Ubuntu or Debian: apt

```bash
sudo apt install python3-full
```

### Verify your installation

```bash
python3 --version
```

```bash
python3 -c "print('Hello from the Space Camp')"
```

When the greeting appears, move on to saving a file. You don't need extra Python packages for this exercise.

## Save and run your first file

The short test ran code written directly in a command. A file lets you store your code files locally. You can use a Text editor like VS Code in order to write or edit these files. These are also called source code files.

### 1. Make a practice folder

Create a folder named `python-practice` somewhere easy to find, such as Documents. Open a text editor or the code editor and write the code below in a new file.

```python
print("Hello from the Space Camp")
```

Save it inside your practice folder as **`hello.py`**. Python files use `.py` file extension. 

Next, you can open the command prompt on Windows or Terminal in Mac/Linux system and navigate to your practice directory where you save this file.

On the terminal, you can type `python hello.py` or `python3 hello.py` to see the results printed on your terminal.

Next, update the print message and rerun your Python file to see the new result.