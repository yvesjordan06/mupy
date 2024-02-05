from mutation.finders.arith_op_finders import find_arithmetic_operators
from mutation.finders.comp_op_finders import find_comparison_operators
from mutation.finders.const_finders import find_constants
from utils.diff import get_diff
from utils.program_loader import program_loader
from utils.ast import get_ast, get_program_string
from mutation.operators_finders import print_node_type
from utils.visualiser import visualize
from mutation.finders.bool_op_finders import find_bool_operators
from mutation.mutators import bool_op_mutator, comp_op_mutator, const_mutator, arith_op_mutator
from utils.writer import write_to_file

def main():
    print("Hello World!")
    program = program_loader("./demo/test.py")
    print(program)
    ast = get_ast(program)
    program = get_program_string(ast)
    print(ast)
    print_node_type(ast)
    visualize(ast)
    bool_operators = find_bool_operators(ast)
    comp_operators = find_comparison_operators(ast)
    constants = find_constants(ast)
    arithmetique_operators = find_arithmetic_operators(ast)
    print(bool_operators)
    write_to_file("mutated_program.py", 'w', program, "Original Program")



    count = 0
    for arith_op in arithmetique_operators:
        mutations = arith_op_mutator.mutate_arithmetic_operators(arith_op, ast)
        for mutation in mutations:
            s = get_program_string(mutation)
            write_to_file("mutated_program.py", 'a', s, "Arith Op Mutation " + str(count))
            write_to_file("mutated_program.py", 'a', get_diff(program, s), "Differences" + str(count), True)
            count += 1
    return


    count = 0
    for constant in constants:
        mutations = const_mutator.mutate_constants(constant, ast)

        for mutation in mutations:
            s = get_program_string(mutation)
            write_to_file("mutated_program.py", 'a', s, "Constant Mutation " + str(count))
            write_to_file("mutated_program.py", 'a', get_diff(program, s), "Differences" + str(count), True)
            count += 1
    
    return

    count = 0
    for bool_op in bool_operators:
        print(bool_op)
        mutations = bool_op_mutator.replace_bool_op(bool_op, ast)
       
        for mutation in mutations:
            s = get_program_string(mutation)
            print(s)
            write_to_file("mutated_program.py", 'a', s, "Bool Op Mutation " + str(count))
            count += 1
    
    count = 0
    for comp_op in comp_operators:
        
        print(comp_op)
        mutations = comp_op_mutator.replace_comp_op(comp_op, ast)
        for mutation in mutations:
            s = get_program_string(mutation)
            print(s)
            write_to_file("mutated_program.py", 'a', s, "Comp Op Mutation " + str(count))
            write_to_file("mutated_program.py", 'a', get_diff(program, s), "Differences" + str(count), True)
            count += 1
        
    print("Goodbye World!")




if __name__ == "__main__":
    main()