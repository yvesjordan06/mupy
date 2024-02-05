import ast, copy
import ast, copy

def replace_bool_op(bool_op, tree):
    mutations = []
    
    # Replace bool_op with True
    true_ast = copy.deepcopy(tree)
    for node in ast.walk(true_ast):
        if isinstance(node, ast.BoolOp) and node.lineno == bool_op.lineno and node.col_offset == bool_op.col_offset:
            node.values = [ast.Constant(value=True)]
            mutations.append(true_ast)
    
    # Replace bool_op with False
    false_ast = copy.deepcopy(tree)
    for node in ast.walk(false_ast):
        if isinstance(node, ast.BoolOp) and node.lineno == bool_op.lineno and node.col_offset == bool_op.col_offset:
            node.values = [ast.Constant(value=False)]
            mutations.append(false_ast)
    
    # Replace bool_op with 'and' or 'or'
    and_or_ast = copy.deepcopy(tree)
    for node in ast.walk(and_or_ast):
        if isinstance(node, ast.BoolOp) and node.lineno == bool_op.lineno and node.col_offset == bool_op.col_offset:
            if isinstance(node.op, ast.Or):
                node.op = ast.And()
            elif isinstance(node.op, ast.And):
                node.op = ast.Or()
            mutations.append(and_or_ast)
    
    # Replace a or b with one of the operands in the expression
    operand_ast = copy.deepcopy(tree)
    for node in ast.walk(operand_ast):
        if isinstance(node, ast.BoolOp) and node.lineno == bool_op.lineno and node.col_offset == bool_op.col_offset:
            if len(node.values) == 2:
                # Original values
                original_values = node.values

                # Mutation: Replace with the first operand
                node.values = [original_values[0]]
                mutations.append(copy.deepcopy(operand_ast))

                # Restore original values
                node.values = original_values

                # Mutation: Replace with the second operand
                node.values = [original_values[1]]
                mutations.append(copy.deepcopy(operand_ast))

                # Restore original values
                node.values = original_values

                # Mutation: Replace with both operands being the first operand
                node.values = [original_values[0], original_values[0]]
                mutations.append(copy.deepcopy(operand_ast))

                # Restore original values
                node.values = original_values

                # Mutation: Replace with both operands being the second operand
                node.values = [original_values[1], original_values[1]]
                mutations.append(copy.deepcopy(operand_ast))

                # Restore original values
                node.values = original_values

    # Replace a or b with false or true
    false_true_ast = copy.deepcopy(tree)
    for node in ast.walk(false_true_ast):
        if isinstance(node, ast.BoolOp) and node.lineno == bool_op.lineno and node.col_offset == bool_op.col_offset:
            if len(node.values) == 2:
                # Original values
                original_values = node.values

                # Mutation: Replace with False
                node.values = [ast.Constant(value=False), original_values[1]]
                mutations.append(copy.deepcopy(false_true_ast))

                # Restore original values
                node.values = original_values

                # Mutation: Replace with True
                node.values = [ast.Constant(value=True), original_values[1]]
                mutations.append(copy.deepcopy(false_true_ast))

                # Restore original values
                node.values = original_values
    
    return mutations
