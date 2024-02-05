def run_test(test, program):
    merged_string = program + test
    function_names = [name for name in globals() if callable(globals()[name]) and name.startswith('test_')]

    for name in function_names:
        print(name)
        try:
            result = globals()[name](merged_string)
            if not result:
                return name
        except Exception:
            return name

    return None