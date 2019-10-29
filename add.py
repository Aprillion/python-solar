"""Add one to command line input"""

import sys

def add_one(x):
    return x + 1

if __name__ == '__main__':
    number = int(sys.argv[1])
    result = add_one(number)
    print(result)
