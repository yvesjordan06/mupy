import ast

def find_constants(ast_node):
    """
    Finds all constants in the given AST node.

    Args:
        ast_node (ast.AST): The AST node to search for constants.

    Returns:
        list: A list of constant nodes found in the AST node.
    """
    constants = []

    class ConstantVisitor(ast.NodeVisitor):
        def visit_Constant(self, node):
            constants.append(node)
            self.generic_visit(node)

    visitor = ConstantVisitor()
    visitor.visit(ast_node)

    return constants