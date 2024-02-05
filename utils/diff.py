from difflib import Differ

def get_diff(a, b):
    d = Differ()
    return '\n'.join(d.compare(a.splitlines(), b.splitlines()))
