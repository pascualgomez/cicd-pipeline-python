# app/calculadora.py
"""This module provides basic arithmetic operations.

It includes functions for addition,
subtraction, multiplication, and division,
including error handling for division by zero.
"""


def sumar(a, b):
    """Returns the sum of two numbers.

    Args:
        a (float or int): The first number.
        b (float or int): The second number.

    Returns:
        float or int: The sum of a and b.
    """
    return a + b


def restar(a, b):
    """Returns the difference between two numbers.

    Args:
        a (float or int): The first number (minuend).
        b (float or int): The second number (subtrahend).

    Returns:
        float or int: The result of subtracting b from a.
    """
    return a - b


def multiplicar(a, b):
    """Returns the product of two numbers.

    Args:
        a (float or int): The first number.
        b (float or int): The second number.

    Returns:
        float or int: The product of a and b.
    """
    return a * b


def dividir(a, b):
    """Returns the division of two numbers.

    Args:
        a (float or int): The numerator.
        b (float or int): The denominator.

    Returns:
        float: The result of dividing a by b.

    Raises:
        ZeroDivisionError: If the denominator (b) is zero.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
