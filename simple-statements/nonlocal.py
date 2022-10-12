"""
The nonlocal statement
https://docs.python.org/3/reference/simple_stmts.html#the-nonlocal-statement
"""

import math


def main():
    def distance(y) -> float:
        """
        Calculate the distance to an object at position y
        """

        # Use the value from outside this scope
        # (nearest enclosing scope, excluding globals)
        nonlocal x

        return math.sqrt(x ** 2 + y ** 2)

    x = 3

    print('y = 4; distance = ', distance(4))
    print('x =', x)

    print('y = 4; distance = ', distance(4))
    print('x =', x)


if __name__ == '__main__':
    main()
