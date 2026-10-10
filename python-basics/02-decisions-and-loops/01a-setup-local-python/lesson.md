---
title: "Set up Python Locally"
slug: setup-local-python
order: 1
language: python
lesson_type: informational
summary: Set up your Python environment in Windows, Linux and Mac.
seo_title: "Setup Python | Python Basics"
seo_description: How to install Python locally on Mac, Linux and Windows. This lesson helps you learn how to set up your Python interpreter locally.
seo_keywords: [python 3 setup, install python, python installation]
---

# How to Install Python?

So far you've used Python on the browser, but what if you want to run Python on your own computer? Depending your your operating system, you can install Python using one of the following instructions. This will allow you to run more advanced programs and also allows you to write your custom Python code.

## Linux / Mac

For Linux and MacOS systems, Python 3 usually comes pre-installed with the operating system. You can check your Python version using following command:

```bash
python3 --version
```

If you want to install Python 3, you can simply use one of the available package managers. For example, on Ubuntu you can use:

```bash
sudo apt-get install python3
```

On Mac, you can use Homebrew.

```bash
brew install python3
```

## Windows

If you are using Windows, you can download and install Python 3 from [python.org](https://www.python.org/downloads/). Once you've installed the Python, you can open your command prompt and type `python --version` to check your Python version.

## Running Python code locally

Let's also take a look at how to execute Python programs on your system. 

Navigate to a directory where you want to store your Python code. You could use a code editor like Visual Studio Code (VS code) to write Python code.Create a new file in this directory with name `hello.py` and add the content from below code. 

```python
print("Hello World")
```

Make sure to save your changes in the file. Now, to execute this code, you can either use Code Runner which comes with Visual Studio Code or on command prompt or terminal, navigate to your directory and type below command.

```shell
python hello.py
```

You will see "Hello World" text printed in the console.
