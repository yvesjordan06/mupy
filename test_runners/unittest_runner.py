import unittest
import types
import importlib.util, sys

from utils.import_module_from_str import import_module_from_string

def run_tests(test_code, program_code):
    class CustomTestRunner:
        def __init__(self, program_code, test_module):
            self.program_code = program_code
            self.test_module = test_module
            self.failed_tests = []

        def run_tests(self):
            # Execute the program code to make its functions available
            exec(self.program_code, globals())

             # Replace the original program's module with the modified program's module
            sys.modules['program_module'] = import_module_from_string('program_module', self.program_code)


            # Discover and run the tests using the custom loader
            loader = unittest.TestLoader()
            suite = loader.loadTestsFromModule(self.test_module)
            result = unittest.TextTestRunner().run(suite)

            # Collect information about failed tests
            for test_case, test_result in result.failures + result.errors:
                test_name = test_case.id().split('.')[-1]
                self.failed_tests.append(test_name)

            return self.failed_tests

    # Create a module from the program code
    #program_module = import_module_from_string('program_module', program_code)
    # Create a module from the test code
    test_module = import_module_from_string('test_module', test_code + '\n' + program_code)

    # Run the tests
    runner = CustomTestRunner(program_code, test_module)
    failed_tests = runner.run_tests()

    return failed_tests