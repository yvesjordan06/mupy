import argparse
from mutation.finders.arith_op_finders import find_arithmetic_operators
from mutation.finders.bool_op_finders import find_bool_operators
from mutation.finders.comp_op_finders import find_comparison_operators
from mutation.finders.const_finders import find_constants

from mutation.mutators import arith_op_mutator, bool_op_mutator, comp_op_mutator, const_mutator
from utils import program_loader, ast, writer, diff
from test_runners import my_oracle_runner, unittest_runner
from mutation.finders import *

def main():
    parser = argparse.ArgumentParser(description='CLI program')
    parser.add_argument('program_path', type=str, help='Path to the program')
    parser.add_argument('test_path', type=str, help='Path to the test')
    parser.add_argument('--mutant_operators', type=str, help='Comma-separated values of mutant operators')

    args = parser.parse_args()

    program_path = args.program_path
    test_path = args.test_path
    mutant_operators = args.mutant_operators.split(',') if args.mutant_operators else []

    # Your code here
    program = program_loader.program_loader(program_path)
    test = program_loader.program_loader(test_path)


    ast_program = ast.get_ast(program)
    ast_test = ast.get_ast(test)

    program = ast.get_program_string(ast_program)
    test = ast.get_program_string(ast_test)

    # Generate the mutants
    nodes = find_arithmetic_operators(ast_program)
    nodes += find_bool_operators(ast_program)
    nodes += find_comparison_operators(ast_program)
    nodes += find_constants(ast_program)


    mutations = []

    for node in nodes:
        mutations += arith_op_mutator.mutate_arithmetic_operators(node, ast_program)
        mutations += bool_op_mutator.replace_bool_op(node, ast_program)
        mutations += comp_op_mutator.replace_comp_op(node, ast_program)
        mutations += const_mutator.mutate_constants(node, ast_program)
    
    # Remove syntax equivalent mutants
    mutation_programs = [ast.get_program_string(mutation) for mutation in mutations]
    mutation_programs = list(set(mutation_programs))

    # Remove syntax equivalent mutants to the original program
    mutation_programs = [mutation for mutation in mutation_programs if mutation != program]

    # Test the original program to get the expected output
    expected_output = unittest_runner.run_tests(test, program)

    # If the original program fails, then the mutants are not useful
    if len(expected_output) > 0:
        print('Original program failed the test, no mutants generated '+ str(expected_output) )
        return
    else:
        print('Original program passed the test')
        
    
    writer.write_to_file('./not_killed.py', 'w', program, 'Original program')


    points = 0
    # Test the mutants
    for mutation in mutation_programs:
        output = unittest_runner.run_tests(test, mutation)
        if len(output) > 0:
            print(f'Mutant Killed by the test suite')
            points += 1
        else:
            print(f'Mutant  Survived the test suite')
            writer.write_to_file('./not_killed.py', 'a', diff.get_diff(program, mutation), 'Mutant Survived by the test suite', True)
    print(f'Points: {points}/{len(mutation_programs)}')




if __name__ == '__main__':
    print('Running main')
    main()
