import ast

def find_comparison_operators(ast_node):
    """
    Finds all comparison operators in the given AST node.

    Args:
        ast_node (ast.AST): The AST node to search for comparison operators.

    Returns:
        list: A list of comparison operator nodes found in the AST node.
    """
    comparison_operators = []

    class ComparisonOperatorVisitor(ast.NodeVisitor):
        def visit_Compare(self, node):
            comparison_operators.append(node)
            self.generic_visit(node)

    visitor = ComparisonOperatorVisitor()
    visitor.visit(ast_node)

    return comparison_operators
