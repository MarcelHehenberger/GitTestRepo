
import pytest


# Calculator functions
def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero")
    return a / b


# Tests
def test_add():
    assert add(5, 3) == 8


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


if __name__ == "__main__":
    print("Calculator Test")
    print("5 + 3 =", add(5, 3))
    print("10 - 4 =", subtract(10, 4))
    print("4 * 3 =", multiply(4, 3))
    print("10 / 2 =", divide(10, 2))
