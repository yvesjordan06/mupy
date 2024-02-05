import ast

def print_node_type(node):
    if isinstance(node, ast.FunctionDef):
        print("Node type: Function")
    elif isinstance(node, ast.Assign):
        print("Node type: Variable Assignment")
    elif isinstance(node, ast.Name):
        print("Node type: Variable")
    elif isinstance(node, ast.Import):
        print("Node type: Import")
    elif isinstance(node, ast.ImportFrom):
        print("Node type: Import From")
    elif isinstance(node, ast.ClassDef):
        print("Node type: Class")
    else:
        print("Node type: Unknown")
        
