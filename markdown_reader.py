import sys

def read_markdown_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            return file.read()
    except UnicodeDecodeError:
        try:
            with open(file_path, 'r', encoding='utf-16') as file:
                return file.read()
        except UnicodeDecodeError:
            raise ValueError("Unable to decode the file. Ensure it is in UTF-16 encoding.")
        except FileNotFoundError:
            raise FileNotFoundError("File not found.")
        except Exception as e:
            raise RuntimeError(f"Error: {e}")
    except FileNotFoundError:
        raise FileNotFoundError("File not found.")
    except Exception as e:
        raise RuntimeError(f"Error: {e}")
    