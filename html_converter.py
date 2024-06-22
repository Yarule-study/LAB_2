import re
import sys

def validate(markdown_text):
    invalid_patterns = [
        r'\*\*.*`.*_.*`.*\*\*',
        r'`.*\*\*.*_.*\*\*.*`',
        r'_.*\*\*.*`.*\*\*.*_'
    ]
    for pattern in invalid_patterns:
        if re.search(pattern, markdown_text):
            return False

    balanced_syntax = [
        ('**', markdown_text.count('**')),
        ('_', markdown_text.count('_')),
        ('`', markdown_text.count('`')),
        ('```', markdown_text.count('```'))
    ]
    return all(count % 2 == 0 for _, count in balanced_syntax)

def convert_markdown_to_html(markdown_text):
    if not validate(markdown_text):
        print("Error: invalid markdown", file=sys.stderr)
        sys.exit(1)

    markdown_text = re.sub(r'```(.*?)```', r'<pre>\1</pre>', markdown_text, flags=re.DOTALL)
    markdown_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown_text)
    markdown_text = re.sub(r'_(.*?)_', r'<i>\1</i>', markdown_text)
    markdown_text = re.sub(r'`(.*?)`', r'<tt>\1</tt>', markdown_text)

    paragraphs = markdown_text.split('\n\n')
    html_content = ''.join(f'<p>{p.replace("\n", " ")}</p>' for p in paragraphs)
    
    return html_content
