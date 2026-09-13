import pytest

from learning_py.calculator import add_numbers


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (-5, -3, -8),
        (1_000_000, 1_000_000, 2_000_000),
    ],
)
def test_add_numbers_sums_its_arguments(a: int, b: int, expected: int) -> None:
    assert add_numbers(a, b) == expected
