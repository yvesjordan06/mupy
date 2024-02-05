import ast

def find_bool_operators(ast_node):
    """
    Finds all boolean operators in the given AST node.

    Args:
        ast_node (ast.AST): The AST node to search for boolean operators.

    Returns:
        list: A list of boolean operator nodes found in the AST node.
    """
    bool_operators = []

    class BoolOperatorVisitor(ast.NodeVisitor):
        def visit_BoolOp(self, node):
            bool_operators.append(node)
            self.generic_visit(node)

    visitor = BoolOperatorVisitor()
    visitor.visit(ast_node)

    return bool_operators
