import sys
import os
from markdown_reader import read_markdown_file
from html_converter import markdown_to_html
from ansi_converter import markdown_to_ansi

def main():
    try:
        if len(sys.argv) < 2:
            raise ValueError("Usage: python main.py <input_markdown_file> [--out <output_file>] [--format <html|ansi>]")

        input_file = sys.argv[1]
        markdown_content = read_markdown_file(input_file)
        
        output_file = None
        output_format = 'ansi'
        
        if '--out' in sys.argv:
            output_file_index = sys.argv.index('--out') + 1
            if output_file_index >= len(sys.argv):
                raise ValueError("Please specify the output file path.")
            output_file = sys.argv[output_file_index]
            output_format = 'html'

        if '--format' in sys.argv:
            format_index = sys.argv.index('--format') + 1
            if format_index >= len(sys.argv):
                raise ValueError("Please specify the format (html or ansi).")
            output_format = sys.argv[format_index]

        if output_format == 'html':
            formatted_content = markdown_to_html(markdown_content)
        elif output_format == 'ansi':
            formatted_content = markdown_to_ansi(markdown_content)
        else:
            raise ValueError("Unsupported format. Use 'html' or 'ansi'.")

        if output_file:
            try:
                with open(output_file, 'w', encoding='utf-8') as file:
                    file.write(formatted_content)
                print(f"Output written to {output_file}")
            except Exception as e:
                raise RuntimeError(f"Error: {e}")
        else:
            print(formatted_content)

    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}", file=sys.stderr)
        sys.exit(1)
    except RuntimeError as re:
        print(f"Error: {re}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
