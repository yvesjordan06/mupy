import ast

def get_ast(code):
    """
    Returns the Abstract Syntax Tree (AST) for the given Python code.

    Args:
        code (str): The Python code string.

    Returns:
        ast.AST: The Abstract Syntax Tree (AST) for the code.
    """
    return ast.parse(code)



def get_program_string(ast_node):
    """
    Returns the program string for the given AST node.

    Args:
        ast_node (ast.AST): The AST node.

    Returns:
        str: The program string.
    """
    return ast.unparse(ast_node)
