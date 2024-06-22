import re

def markdown_to_html(markdown_text):
    validate_markdown(markdown_text)

    markdown_text = re.sub(r'```(.*?)```', r'<pre>\1</pre>', markdown_text, flags=re.DOTALL)
    markdown_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown_text)
    markdown_text = re.sub(r'_(.*?)_', r'<i>\1</i>', markdown_text)
    markdown_text = re.sub(r'`(.*?)`', r'<tt>\1</tt>', markdown_text)

    paragraphs = markdown_text.split('\n\n')
    html_content = ''.join(f'<p>{p.replace("\n", " ")}</p>' for p in paragraphs)
    
    return html_content

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
