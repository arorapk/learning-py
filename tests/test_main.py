import pytest

from learning_py import main


def test_main_greets(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    captured = capsys.readouterr()
    assert "Hello from learning-py!" in captured.out
