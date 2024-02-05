import ast

def find_arithmetic_operators(ast_node):
    """
    Finds all arithmetic operators in the given AST node.

    Args:
        ast_node (ast.AST): The AST node to search for arithmetic operators.

    Returns:
        list: A list of arithmetic operator nodes found in the AST node.
    """
    arithmetic_operators = []

    class ArithmeticOperatorVisitor(ast.NodeVisitor):
        def visit_BinOp(self, node):
            arithmetic_operators.append(node)
            self.generic_visit(node)
        
        def visit_UnaryOp(self, node):
            arithmetic_operators.append(node)
            self.generic_visit(node)
        
        def visit_AugAssign(self, node):
            arithmetic_operators.append(node)
            self.generic_visit(node)

    visitor = ArithmeticOperatorVisitor()
    visitor.visit(ast_node)

    return arithmetic_operators