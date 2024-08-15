"""File Management"""

import os
import json


def create(file_name: str, content: list | dict = None) -> None:
    """Create a JSON file with a lis or dict type"""
    # Ternario
    mode = "w" if content else "x"
    try:
        file = open(file_name, mode)

    except FileExistsError as error:
        raise OSError(f"File '{file_name}' already exists") from error

    except PermissionError as error:
        raise OSError(f"You do not have permission to create '{file_name}'") from error

    if content:
        json_content = json.dumps(content)
        file.write(json_content)

    file.close()


def update(file_name: str, content: list | dict, overwrite: bool = False) -> None:
    """Create a file if content is none or create a file with content if apply"""
    if not isinstance(content, list) or isinstance(content, dict):
        raise ValueError("'content' arguments must be specified")

    mode = "w" if overwrite else "a"
    file = open(file_name, mode)
    json_content = json.dumps(content)
    file.write(json_content)
    file.close()


def read(file_name: str) -> list | dict:
    """Returns the Content of a text file
    Args:
        file_name (str): File name or path
    Returns (str): File content
    """
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"File {file_name} was not found")

    json_file = open(file_name)
    file = json.loads(json_file)
    content = file.read()
    file.close()
    return content
