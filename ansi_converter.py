import re

def markdown_to_ansi(markdown_text):
    validate_markdown(markdown_text)

    markdown_text = re.sub(r'```(.*?)```', r'\033[7m\1\033[0m', markdown_text, flags=re.DOTALL)
    markdown_text = re.sub(r'\*\*(.*?)\*\*', r'\033[1m\1\033[0m', markdown_text)
    markdown_text = re.sub(r'_(.*?)_', r'\033[3m\1\033[0m', markdown_text)
    markdown_text = re.sub(r'`(.*?)`', r'\033[7m\1\033[0m', markdown_text)

    paragraphs = markdown_text.split('\n\n')
    ansi_content = ''.join(f'{p.replace("\n", " ")}\n' for p in paragraphs)
    
    return ansi_content

def validate_markdown(markdown_text):
    if re.search(r'\*\*.*`.*_.*`.*\*\*', markdown_text) or \
       re.search(r'`.*\*\*.*_.*\*\*.*`', markdown_text) or \
       re.search(r'_.*\*\*.*`.*\*\*.*_', markdown_text):
        raise ValueError("Invalid markdown")

    balanced_syntax = [
        ('**', markdown_text.count('**')),
        ('_', markdown_text.count('_')),
        ('`', markdown_text.count('`')),
        ('```', markdown_text.count('```'))
    ]
    if any(count % 2 != 0 for _, count in balanced_syntax):
        raise ValueError("Unbalanced markdown syntax")
