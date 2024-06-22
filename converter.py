import re
import sys

def is_valid_markdown(text):
    patterns = [
        r'\*\*.*`.*_.*`.*\*\*',
        r'`.*\*\*.*_.*\*\*.*`',
        r'_.*\*\*.*`.*\*\*.*_'
    ]
    
    for pattern in patterns:
        if re.search(pattern, text):
            return False
    
    counts = {
        '**': text.count('**'),
        '_': text.count('_'),
        '`': text.count('`'),
        '```': text.count('```')
    }
    
    return all(count % 2 == 0 for count in counts.values())

def markdown_to_html(markdown_text):
    if not is_valid_markdown(markdown_text):
        sys.stderr.write("Error: Invalid markdown\n")
        sys.exit(1)
    
    preformatted_blocks = re.findall(r'```(.*?)```', markdown_text, re.DOTALL)
    for block in preformatted_blocks:
        markdown_text = markdown_text.replace(f'```{block}```', f'<pre>{block}</pre>')

    conversions = {
        r'\*\*(.*?)\*\*': r'<b>\1</b>',
        r'_(.*?)_': r'<i>\1</i>',
        r'`(.*?)`': r'<tt>\1</tt>'
    }

    for pattern, replacement in conversions.items():
        markdown_text = re.sub(pattern, replacement, markdown_text)
    
    paragraphs = markdown_text.split('\n\n')
    html_text = ''.join([f'<p>{p.replace("\n", " ")}</p>' for p in paragraphs])
    
    return html_text
