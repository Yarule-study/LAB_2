import subprocess
import pytest

@pytest.fixture
def prepare_markdown_file(tmp_path):
    markdown_content = "**bold text**\n\n_italic text_\n\n`monospace text`\n\n```preformatted block```"
    markdown_file = tmp_path / "sample.md"
    with open(markdown_file, 'w', encoding='utf-8') as file:
        file.write(markdown_content)
    return markdown_file

def test_markdown_to_html(prepare_markdown_file, tmp_path):
    html_file = tmp_path / "output.html"

    result = subprocess.run(['python', 'main.py', str(prepare_markdown_file), '--out', str(html_file), '--format', 'html'],
                            capture_output=True, text=True)
    assert result.returncode == 0

    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    assert '<b>bold text</b>' in html_content
    assert '<i>italic text</i>' in html_content
    assert '<tt>monospace text</tt>' in html_content
    assert '<pre>preformatted block</pre>' in html_content
