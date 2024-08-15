"""File Management"""

import os
import json


def create(file_name: str, content: list | dict = None) -> None:
    """Create a JSON file with a lis or dict type"""
    # Ternario
    mode = "w" if content else "x"
    try:
        file = open(file_name, mode, encoding="utf-8")

    except FileExistsError as error:
        raise OSError(f"File '{file_name}' already exists") from error

    except PermissionError as error:
        raise OSError(f"You do not have permission to create '{file_name}'") from error

    if content and isinstance(content, (list, dict)):
        content = json.dumps(content)
        file.write(content)

    file.close()


def update(file_name: str, content: list | dict, overwrite: bool = False) -> None:
    """Update a JSON file"""
    if not isinstance(content, (list, dict)):
        raise TypeError("'content' must be a list or dict type")

    if overwrite:
        file_content = content

    elif not overwrite:
        file = open(file_name, encoding="utf-8")
        file_content = json.loads(file.read())
        file.close()

        if isinstance(file_content, list):
            if isinstance(content, list):
                file_content.extend(content)

            elif isinstance(content, dict):
                file_content.append(content)

        elif isinstance(file_content, dict):
            if isinstance(content, list):
                file_content = [file_content] + content

            elif isinstance(content, dict):
                file_content = [file_content, content]

    file = open(file_name, "w", encoding="utf-8")
    file.write(json.dumps(file_content))
    file.close()


def read(file_name: str) -> list | dict:
    """Returns the Content of a text file
    Args:
        file_name (str): File name or path
    Returns (str): File content
    """
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"File {file_name} was not found")

    json_file = open(file_name, encoding="utf-8")
    # file = json.loads(json_file)
    content = json_file.read()
    json_file.close()
    return content
