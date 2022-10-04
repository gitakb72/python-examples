factorial_lambda = lambda num: num * factorial_lambda(num - 1) if num >= 2 else 1
"lambdas are simple functions that can be expressed in 1 line"""

def factorial_function(num: int) -> int:
    """regular functions can be as complicated as you like"""
    if num == 1:
        return 1
    return num * factorial(num - 1)

assert factorial_function(6) == factorial_lambda(6)
