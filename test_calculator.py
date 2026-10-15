import pytest

from calculator import add, calculate, divide, multiply, subtract


@pytest.mark.parametrize(
    ("operation", "first", "second", "expected"),
    [
        (add, 2, 3, 5),
        (subtract, 7, 4, 3),
        (multiply, 3, 4, 12),
        (divide, 8, 2, 4),
        (add, -2, 3, 1),
        (divide, 5, 2, 2.5),
    ],
)
def test_arithmetic_operations(operation, first, second, expected):
    assert operation(first, second) == expected


@pytest.mark.parametrize(
    ("operation", "expected"),
    [
        ("add", 9),
        ("subtract", 3),
        ("multiply", 18),
        ("divide", 2),
    ],
)
def test_calculate_dispatches_operation(operation, expected):
    assert calculate(operation, 6, 3) == expected


def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)


def test_calculate_rejects_unknown_operation():
    with pytest.raises(ValueError, match="Unsupported operation"):
        calculate("power", 2, 3)
