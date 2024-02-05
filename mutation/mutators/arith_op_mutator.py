import ast
import copy

def mutate_arithmetic_operators(arith_op, tree):
    mutations = []

    # Replace arith_op with '+'
    add_ast = copy.deepcopy(tree)
    for node in ast.walk(add_ast):
        if isinstance(node, (ast.BinOp, ast.AugAssign)) and node.lineno == arith_op.lineno and node.col_offset == arith_op.col_offset:
            node.op = ast.Add()
            mutations.append(add_ast)

    # Replace arith_op with '-'
    sub_ast = copy.deepcopy(tree)
    for node in ast.walk(sub_ast):
        if isinstance(node, (ast.BinOp, ast.AugAssign)) and node.lineno == arith_op.lineno and node.col_offset == arith_op.col_offset:
            node.op = ast.Sub()
            mutations.append(sub_ast)

    # Replace arith_op with '*'
    mult_ast = copy.deepcopy(tree)
    for node in ast.walk(mult_ast):
        if isinstance(node, (ast.BinOp, ast.AugAssign)) and node.lineno == arith_op.lineno and node.col_offset == arith_op.col_offset:
            node.op = ast.Mult()
            mutations.append(mult_ast)

    # Replace arith_op with '/'
    div_ast = copy.deepcopy(tree)
    for node in ast.walk(div_ast):
        if isinstance(node, (ast.BinOp, ast.AugAssign)) and node.lineno == arith_op.lineno and node.col_offset == arith_op.col_offset:
            node.op = ast.Div()
            mutations.append(div_ast)

    # Replace arith_op with '%'
    mod_ast = copy.deepcopy(tree)
    for node in ast.walk(mod_ast):
        if isinstance(node, (ast.BinOp, ast.AugAssign)) and node.lineno == arith_op.lineno and node.col_offset == arith_op.col_offset:
            node.op = ast.Mod()
            mutations.append(mod_ast)

    # Replace arith_op with a constant value (e.g., 0)
    zero_ast = copy.deepcopy(tree)
    for node in ast.walk(zero_ast):
        if isinstance(node, ast.BinOp) and node.lineno == arith_op.lineno and node.col_offset == arith_op.col_offset:
            node.right = ast.Constant(value=0)
            mutations.append(zero_ast)

    return mutations