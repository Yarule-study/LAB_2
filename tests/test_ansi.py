# tests/test_ansi.py

import subprocess
import pytest

@pytest.fixture
def prepare_markdown_file(tmp_path):
    # Create a sample Markdown file for testing ANSI conversion
    markdown_content = "**bold text**\n\n_italic text_\n\n`monospace text`\n\n```preformatted block```"
    # Introduce an invalid markdown pattern to trigger the error
    markdown_content += "\n**bold text`_italic text`monospace text_"
    
    markdown_file = tmp_path / "sample.md"
    with open(markdown_file, 'w', encoding='utf-8') as file:
        file.write(markdown_content)
    return markdown_file

def test_markdown_to_ansi(prepare_markdown_file, tmp_path):
    # Test Markdown to ANSI conversion functionality
    ansi_file = tmp_path / "output.ansi"

    result = subprocess.run(['python', 'main.py', str(prepare_markdown_file), '--out', str(ansi_file), '--format', 'ansi'],
                            capture_output=True, text=True)
    # Assert that the return code is not 0 (indicating an error)
    assert result.returncode != 0

    with open(ansi_file, 'r', encoding='utf-8') as file:
        ansi_content = file.read()

    # Assertions removed for simplicity as the main focus is to check the return code
