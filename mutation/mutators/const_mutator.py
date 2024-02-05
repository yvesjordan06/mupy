import ast
import copy

def mutate_constants(const_node, tree):
    mutations = []

    if isinstance(const_node, ast.Num):  # Mutate numerical constants
        # Mutation: Replace with 0
        zero_ast = copy.deepcopy(tree)
        for node in ast.walk(zero_ast):
            if isinstance(node, ast.Num) and node.lineno == const_node.lineno and node.col_offset == const_node.col_offset:
                node.n = 0
                mutations.append(zero_ast)

        # Mutation: Replace with abs(x)
        abs_ast = copy.deepcopy(tree)
        for node in ast.walk(abs_ast):
            if isinstance(node, ast.Num) and node.lineno == const_node.lineno and node.col_offset == const_node.col_offset:
                node.n = abs(node.n)
                mutations.append(abs_ast)

        # Mutation: Replace with -abs(x)
        neg_abs_ast = copy.deepcopy(tree)
        for node in ast.walk(neg_abs_ast):
            if isinstance(node, ast.Num) and node.lineno == const_node.lineno and node.col_offset == const_node.col_offset:
                node.n = -abs(node.n)
                mutations.append(neg_abs_ast)

    elif isinstance(const_node, ast.Str):  # Mutate string constants
        # Mutation: Replace with an empty string
        empty_str_ast = copy.deepcopy(tree)
        for node in ast.walk(empty_str_ast):
            if isinstance(node, ast.Str) and node.lineno == const_node.lineno and node.col_offset == const_node.col_offset:
                node.s = ""
                mutations.append(empty_str_ast)

    elif isinstance(const_node, (ast.NameConstant, ast.Constant)):  # Mutate boolean and None constants
        # Mutation: Negate boolean or replace None with True
        negate_ast = copy.deepcopy(tree)
        for node in ast.walk(negate_ast):
            if (isinstance(node, ast.NameConstant) or isinstance(node, ast.Constant)) and \
               node.lineno == const_node.lineno and node.col_offset == const_node.col_offset:
                if node.value is True:
                    node.value = False
                elif node.value is False:
                    node.value = True
                elif node.value is None:
                    node.value = True
                mutations.append(negate_ast)

    return mutations