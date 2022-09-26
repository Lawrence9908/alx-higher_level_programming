#!/usr/bin/python3

if __name__ == "__main__":
    """Handle basic arithmentics operations"""

    from calculator_1 import add, sub, mul, div
    import sys
    
    length = len(sys.argv) -1
    
    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    opa = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(opa.keys()):
        print("Unknown operator. Available operators: +, -, *, and /")
        sys.exit(1)
    
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, opa[sys.argv[2]](a, b)))

