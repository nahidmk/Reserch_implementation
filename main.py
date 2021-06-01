
from pyflowchart import Flowchart

# >>> with open('simple.py') as f:
# ...     code = f.read()
# ...
# >>> fc = Flowchart.from_code(code)
# >>> print(fc.flowchart())
def print_hi(name):
    with open('Simple.py') as f:
        code = f.read()
    print("code- >",code)
    fc = Flowchart.from_code(code)
    print(fc.flowchart())


if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
