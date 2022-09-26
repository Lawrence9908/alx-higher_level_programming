#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the addition of all arguments."""

    import sys
    
    total_number = 0
    for i in range(len(sys.argv) - 1):
        total_number += int(sys.argv[i +1])
    print("{}".format(total_nnumber))
