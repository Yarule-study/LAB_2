import sys
from converter import markdown_to_html

def load_markdown_file(path):
    encodings = ['utf-8-sig', 'utf-16']
    for encoding in encodings:
        try:
            with open(path, 'r', encoding=encoding) as file:
                return file.read()
        except FileNotFoundError:
            sys.stderr.write(f"Error: File not found - {path}\n")
            sys.exit(1)
        except UnicodeDecodeError:
            continue
        except Exception as e:
            sys.stderr.write(f"Error: {e}\n")
            sys.exit(1)
    sys.stderr.write("Error: Unable to decode the file. Supported encodings: utf-8-sig, utf-16\n")
    sys.exit(1)

def convert_markdown(input_path, output_path=None):
    markdown_text = load_markdown_file(input_path)
    html_text = markdown_to_html(markdown_text)
    if output_path:
        try:
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(html_text)
            print(f"HTML output written to {output_path}")
        except Exception as e:
            sys.stderr.write(f"Error: {e}\n")
            sys.exit(1)
    else:
        print(html_text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: python main.py <input_markdown_file> [--out <output_html_file>]\n")
        sys.exit(1)
    
    input_md_file = sys.argv[1]
    output_html_file = None
    
    if len(sys.argv) > 2:
        if sys.argv[2] == '--out' and len(sys.argv) == 4:
            output_html_file = sys.argv[3]
        else:
            sys.stderr.write("Error: Invalid arguments. Usage: python main.py <input_markdown_file> [--out <output_html_file>]\n")
            sys.exit(1)
    
    convert_markdown(input_md_file, output_html_file)
    