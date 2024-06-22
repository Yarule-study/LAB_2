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

3. **The program will output the HTML** to the standard output or save it to the specified file.
