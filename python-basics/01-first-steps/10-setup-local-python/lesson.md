---
title: "Optional: Set up Python Locally"
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

You've already run Python in the course. Installing it on your computer lets you run your own saved programs without opening a lesson.

This is an optional detour. You can finish the whole course in the browser. If you're using a school or work computer that doesn't allow installations, continue to the section quiz instead.

Choose the instructions for **your operating system only**, then finish with **Save and run your first file** below.

| Your computer | Installation route |
| --- | --- |
| Windows | Python Install Manager, followed by a Python runtime |
| macOS | Homebrew, a tool that installs software from your terminal |
| Linux | Your distribution's package manager: `apt` or `dnf` |

A **terminal** is an app where you type commands for your computer. The installation commands below belong there, not in the course's Python editor. Run one command at a time and wait for it to finish before entering the next.

## Windows: install Python

### 1. Get the official installer

Open the official Python downloads page in your browser:

`https://www.python.org/downloads/`

Choose **Python Install Manager** for Windows. Open the downloaded installer and select **Install**. You can also install the same manager through the Microsoft Store; check that the publisher is **Python Software Foundation**.

You don't need an embeddable package or the Python source code.

### 2. Install the part that runs your code

Once the manager is installed, close any terminals you already had open. Open **Start**, search for **PowerShell**, and open it normally.

Enter:

```powershell
pymanager install default
```

The manager downloads and installs its default Python release. Wait until the command finishes and the PowerShell prompt returns. Installing the manager and installing Python itself are separate steps.

### 3. Check your installation

In that same PowerShell window, run:

```powershell
python --version
```

You should see a version beginning with `Python 3`. The remaining numbers depend on the release you installed; they don't need to match a screenshot or another learner's computer.

Then try a small program:

```powershell
python -c "print('Hello from Spawn Camp')"
```

The `-c` option runs the Python code inside the quotes. Look for `Hello from Spawn Camp` on its own line. You're ready to run a file.

### If a Windows command isn't found

- **`pymanager` isn't recognized:** close and reopen PowerShell after installation. Check that Python Install Manager appears in Windows **Installed apps**.
- **`python` opens the Store or isn't recognized:** try `pymanager exec --version`. If that works, search Start for **Manage app execution aliases** and check the Python Install Manager aliases. The official Windows guide below has the detailed alias and PATH checks.
- **An older `py` command doesn't understand `install`:** use `pymanager install default` as shown above; an older Python launcher can also use the name `py`.

Don't remove an existing Python installation just to follow this lesson. If `python --version` already reports Python 3 and the small program runs, you can skip installing another copy.

## macOS: install with Homebrew

Some Macs have Python through developer tools; others don't. Don't assume it's installed, and don't remove an Apple-managed Python to make room for your own.

### 1. Open Terminal and check

Press **Command + Space**, type **Terminal**, and open it. Enter:

```bash
python3 --version
```

If you get a Python 3 version, try the test in step 4. You can skip installation if it works. If Python is missing or macOS offers to install developer tools, continue below.

### 2. Make Homebrew available

Homebrew is a package manager: you name the software you want, and it handles downloading and installing it.

Check whether you already have it:

```bash
brew --version
```

If that prints a Homebrew version, go to step 3.

Otherwise, open Homebrew's official installation page:

`https://brew.sh/`

Copy the command under **Install Homebrew** into Terminal and run it. Read the changes it proposes before confirming. Follow its prompts, including any request to install Apple's Command Line Tools. If it asks for your Mac login password, type it into Terminal; the characters won't appear as you type.

At the end, follow the printed **Next steps**, especially the commands that add Homebrew to your shell. They depend on your Mac, so copy the ones your installer displays. Open a new Terminal window and check `brew --version` again.

### 3. Install Python

Run these commands separately:

```bash
brew update
```

```bash
brew install python
```

The first refreshes Homebrew's package information. The second installs Python. You don't need to put `sudo` in front of these commands.

### 4. Run a small program

```bash
python3 --version
```

```bash
python3 -c "print('Hello from Spawn Camp')"
```

Look for a Python 3 version and then your greeting. Use `python3`, rather than `python`, for the macOS commands in this lesson.

If Homebrew doesn't support your macOS version, check the requirements of the official macOS installer on Python's downloads page rather than forcing an unsupported Homebrew installation.

## Linux: use your distribution's package manager

Many Linux distributions include Python 3 for system tools. Open your terminal and check:

```bash
python3 --version
```

If it reports Python 3, try the small program below before installing anything. Don't uninstall the system's Python; other tools may depend on it.

If Python is missing, use **only the command group for your distribution**.

### Ubuntu or Debian: apt

```bash
sudo apt update
```

```bash
sudo apt install python3-full
```

`apt update` refreshes the available-package list. `python3-full` installs Python with its standard library and tools for local development.

### Fedora: dnf

```bash
sudo dnf install python3
```

`sudo` asks for permission to install system software. Enter your own account password in the terminal if prompted; it won't show characters as you type. Review the package list, then confirm the installation when asked. If you don't have permission on a managed computer, ask its administrator instead of trying to bypass it.

Other Linux distributions use different commands. Use your distribution's Python installation guide rather than trying `apt` and `dnf` at random.

### Check the result

```bash
python3 --version
```

```bash
python3 -c "print('Hello from Spawn Camp')"
```

When the greeting appears, move on to saving a file. You don't need extra Python packages for this exercise.

## Save and run your first file

The short test ran code written directly in a command. A file lets you keep a program and edit it later.

### 1. Make a practice folder

Create a folder named `python-practice` somewhere easy to find, such as Documents. Open a plain-text editor or the code editor you already use, and enter:

```python
print("Hello from Spawn Camp")
```

Save it inside your practice folder as **`hello.py`**.

On Windows, if you use Notepad, choose **All files** in the Save As dialog so the filename doesn't become `hello.py.txt`. On macOS, if you use TextEdit, choose **Format → Make Plain Text** before saving. A word processor document isn't a Python file.

### 2. Open a terminal in that folder

In Windows File Explorer, open `python-practice`, click its address bar, type `powershell`, and press Enter. The PowerShell window opens in that folder.

On macOS or Linux, type `cd ` in Terminal, including the space, then drag your practice folder from the file manager into the terminal and press Enter. If your file manager doesn't support dragging, enter `cd` followed by the folder's full path in quotes.

`cd` means **change directory**. It tells the terminal which folder to work in.

### 3. Run the saved program

On Windows:

```powershell
python hello.py
```

On macOS or Linux:

```bash
python3 hello.py
```

You should see:

```text
Hello from Spawn Camp
```

If Python says it **can't open the file**, check that your terminal is in the practice folder and the file is named `hello.py`, not `hello.py.txt`.

If you see a **`>>>` prompt**, you're inside Python's interactive shell rather than your terminal. Enter `exit()` first, then run the file command above.

### 4. Make it yours

Change the greeting in the file to `My first local Python program`. Save, then run the same command again. The new message confirms that you're running the file you just edited.

You now have a saved program you can return to. Your local files and the course editor are separate: come back to the browser for the lessons' **Run** and **Submit** checks. Installing Python isn't graded.

## Official setup references

Use these if your computer behaves differently or an installer screen has changed:

- Windows installation and command troubleshooting: `https://docs.python.org/3/using/windows.html`
- Homebrew installation requirements and alternatives: `https://docs.brew.sh/Installation`
- Python on macOS: `https://docs.python.org/3/using/mac.html`
- Ubuntu's Python setup guide: `https://ubuntu.com/developers/docs/howto/python-setup/`
- Fedora's Python guide: `https://developer.fedoraproject.org/tech/languages/python/python-installation.html`
