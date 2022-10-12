"""
The global statement
https://docs.python.org/3/reference/simple_stmts.html#the-global-statement
"""

import math

x = 3


def distance(y) -> float:
    """
    Calculate the distance to an object at position y
    """

    # Without using global keyword
    # x = 0

    # Using global keyword
    # global x
    # x = 0

    return math.sqrt(x ** 2 + y ** 2)


def main():
    print('y = 4; distance = ', distance(4))
    print('x =', x)

    print('y = 4; distance = ', distance(4))
    print('x =', x)


if __name__ == '__main__':
    main()
