import ast, copy

def replace_comp_op(comp_op, tree):
    mutations = []
    
    # Replace comp_op with a different comparison operator
    comp_op_ast = copy.deepcopy(tree)
    for node in ast.walk(comp_op_ast):
        if isinstance(node, ast.Compare) and node.lineno == comp_op.lineno and node.col_offset == comp_op.col_offset:
            original_ops = node.ops
            original_left = node.left
            original_comparators = node.comparators
           
            if isinstance(node.ops[0], ast.Gt):
                node.ops[0] = ast.Lt()
            elif isinstance(node.ops[0], ast.Lt):
                node.ops[0] = ast.Gt()
            elif isinstance(node.ops[0], ast.GtE):
                node.ops[0] = ast.LtE()
            elif isinstance(node.ops[0], ast.LtE):
                node.ops[0] = ast.GtE()
            elif isinstance(node.ops[0], ast.Eq):
                node.ops[0] = ast.NotEq()
            elif isinstance(node.ops[0], ast.NotEq):
                node.ops[0] = ast.Eq()

            # Append the mutation after the operator replacement
            mutations.append(copy.deepcopy(comp_op_ast))

            # Restore the original operator
            node.ops = original_ops

            # Add ((a op b), false) mutation (l != l)
            node.left = original_left
            node.comparators = [original_left]
            node.ops = [ast.NotEq()]

            mutations.append(copy.deepcopy(comp_op_ast))

            # Add ((a op b), true) mutation (l == l)
            node.ops = [ast.Eq()]
            mutations.append(copy.deepcopy(comp_op_ast))
            
    
    return mutations
