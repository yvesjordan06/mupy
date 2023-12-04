import json


def email_to_folder_name(email):
    """
    This function converts an email address into a folder name.

    It replaces the '@' symbol with '_at_' and the '.' symbol with '_dot_'.

    Args:
        email (str): The email address to be converted.

    Returns:
        str: The converted email address, which can be used as a folder name.
    """
    return email.replace("@", "_at_").replace(".", "_dot_")


def load_json(file_path):
    """
    This function loads a JSON file from the provided file path.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The content of the JSON file as a Python dictionary.
    """
    # print the current working directory
    with open(file_path, "r") as f:
        return json.load(f)


def get_file_name(name):
    """
    This function retrieves the file name from a given string.

    If the string ends with '.py', the string is returned as is.
    Otherwise, '.py' is appended to the string.

    Args:
        name (str): The string to be processed.

    Returns:
        str: The processed string representing the file name.
    """
    if name.endswith(".py"):
        return name
    return name + ".py"