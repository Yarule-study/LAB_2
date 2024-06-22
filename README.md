# Markdown to HTML Converter

## Short Description

Markdown to HTML Converter is a command-line tool that takes a Markdown file and converts it into corresponding HTML. It allows for convenient conversion of Markdown syntax into a web format.

## Build and Run Instructions

1. **Clone the repository:**
    ```bash
    git clone <URL>
    ```
   
2. **Navigate to the project directory:**
    ```bash
    cd <project-directory>
    ```
   
3. **Run the application:**
    ```bash
    python main.py /path/to/file.md
    ```
    **Or save the result to a file:**
    ```bash
    python main.py /path/to/file.md --out /path/to/outputfile.html
    ```

## User Guide

1. **Pass the path to the Markdown file** as a command-line argument when running the program.

2. **Optionally, if you want to save the result to a file,** use the `--out` flag followed by the path to the output HTML file.

3. **Select the `--format` flag** to select the live format (`html` or `ansi`):
    ```bash
    python main.py /path/to/file.md --format ansi
    ```

4. **The program will output the HTML or ANSI** to the standard output or save it to the specified file.

## Instructions for running tests

1. **Make sure you have `pytest` installed.** If not, install it using the command:
    ```bash
    pip install pytest
    ```

2. **Go to the root directory of the project.**

3. **Run the tests:**
    ```bash
    pytest tests/
    ```

## Link to the commit on which the test is expected to fail

**"Introduce error in ANSI test":**
[Link to commit](https://github.com/Yarule-study/LAB_2/actions/runs/9624758029/job/26548899536)

## Links to revert commits

**Revert "Added tests for Markdown to HTML and ANSI conversion":**
[Revert commit link](https://github.com/Yarule-study/LAB_2/commit/0858ef1adb28fe77b157e109356ac58134743f94)

**Revert "Introduce error in ANSI test":**
[Revert commit link](https://github.com/Yarule-study/LAB_2/commit/0a513181d72eb9756a02795a430a894b9259ae61)

## Conclusion

**Unit tests are really useful. They help to quickly identify and correct errors in the code, which saves time and ensures the stability of the program during its development.​**