"""File Management"""

import os


def create(file_name: str, content: str = None) -> None:
    """Create a file if content is none or create a file with content if apply"""
    # Ternario
    mode = "w" if content else "x"
    try:
        file = open(file_name, mode)

    except FileExistsError as error:
        raise OSError(f"File '{file_name}' already exists") from error

    except PermissionError as error:
        raise OSError(f"You do not have permission to create '{file_name}'") from error

    if content:
        file.write(content)

    file.close()


def update(file_name: str, content: str, overwrite: bool = False) -> None:
    """Create a file if content is none or create a file with content if apply"""
    if not isinstance(content, str) or content == "":
        raise ValueError("'content' arguments must be specified")

    mode = "w" if overwrite else "a"
    file = open(file_name, mode)
    file.write(content)
    file.close()


def read(file_name: str) -> str:
    """Returns the Content of a text file
    Args:
        file_name (str): File name or path
    Returns (str): File content
    """
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"File {file_name} was not found")

    file = open(file_name)
    content = file.read()
    file.close()
    return content
