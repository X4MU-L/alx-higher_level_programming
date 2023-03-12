#!/usr/bin/python3

if __name__ == "__main__":
    """Perform a calculator operation according to operator passed to command"""
    import sys
    from calculator_1 import add, sub, mul, div

    operators = ["*","+","/","-"]
    functions = [mul,add,div,sub]
    arg_len = len(sys.argv) - 1
    operator = sys.argv[2]

    if arg_len < 3:
        sys.stderr.write("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    try:
        idx = operators.index(operator)
        print(f'{a:d} {operator} {b:d} = {functions[idx](a, b)}')
    except:
        sys.stderr.write("Unknown operator. "
                         "Available operators: +, -, * and /\n")
        sys.exit(1)
