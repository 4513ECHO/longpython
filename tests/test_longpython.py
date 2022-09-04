from argparse import ArgumentTypeError

import pytest

from longpython.main import check_natural, generate_python


def test_negative() -> None:
    with pytest.raises(ArgumentTypeError):
        check_natural("-1")


def test_zero() -> None:
    assert generate_python(0) == '  _\n(" ヽ\n   \\ \\\n    \\ \\ _ ,\n     \\___/'


def test_even() -> None:
    assert generate_python(4) == '  _\n(" ヽ\n   \\ \\\n   / /\n   \\ \\\n   / /\n   \\ \\\n    \\ \\ _ ,\n     \\___/'


def test_odd() -> None:
    assert generate_python(3) == '  _\n(" ヽ\n   \\ \\\n   / /\n   \\ \\\n   / /\n   \\ \\ _ ,\n    \\___/'
