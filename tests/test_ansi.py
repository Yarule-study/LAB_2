# tests/ansi_tests.py

import subprocess
import pytest

@pytest.fixture
def prepare_markdown_file(tmp_path):
    # Create a sample Markdown file for testing ANSI conversion
    markdown_content = "**bold text**\n\n_italic text_\n\n`monospace text`\n\n```preformatted block```"
    markdown_file = tmp_path / "sample.md"
    with open(markdown_file, 'w', encoding='utf-8') as file:
        file.write(markdown_content)
    return markdown_file

def test_markdown_to_ansi(prepare_markdown_file, tmp_path):
    # Test Markdown to ANSI conversion functionality
    ansi_file = tmp_path / "output.ansi"

    result = subprocess.run(['python', 'main.py', str(prepare_markdown_file), '--out', str(ansi_file), '--format', 'ansi'],
                            capture_output=True, text=True)
    assert result.returncode == 0

    with open(ansi_file, 'r', encoding='utf-8') as file:
        ansi_content = file.read()

    assert '\033[1mbold text\033[0m' in ansi_content
    assert '\033[3mitalic text\033[0m' in ansi_content
    assert '\033[7mmonospace text\033[0m' in ansi_content
    assert '\033[7mpreformatted block\033[0m' in ansi_content
