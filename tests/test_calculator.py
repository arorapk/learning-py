from learning_py.calculator import add_numbers


def test_add_numbers_adds_two_positive_integers() -> None:
    result = add_numbers(2, 3)
    assert result == 5
