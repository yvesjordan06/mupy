def program_loader(path):
    """
    Load a program from a file.

    Args:
        path (str): The path to the file containing the program.

    Returns:
        str: The program string read from the file.
    """
    with open(path, 'r') as file:
        program_string = file.read()
    return program_string
