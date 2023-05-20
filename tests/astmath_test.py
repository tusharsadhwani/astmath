from numbers import Number

import pytest

import astmath


@pytest.mark.parametrize(
    ("source", "output"),
    (
        ("40 + 2", 42),
        ("40 + 4 // 2", 42),
        ("(2 * 4) // (3 + 5) + 10.0", 11.0),
        ('"foo" * 3', "foofoofoo"),
    ),
)
def test_eval(source: str, output: object) -> None:
    """Tests evaluating arithemetic stuff."""
    assert astmath.eval(source) == output


@pytest.mark.parametrize(
    ("source", "error"),
    (
        ("x = 1\nx * 2", "astmath.eval(...) only supports single expressions."),
        ("def foo(): pass", "astmath.eval(...) only supports single expressions."),
        ("a + 2", "astmath.eval(...) doesn't work on non-constants."),
        ("foo", "astmath.eval(...) doesn't work on non-constants."),
    ),
)
def test_astmath_errors(source: str, error: str) -> None:
    with pytest.raises(ValueError) as excinfo:
        astmath.eval(source)

    assert excinfo.value.args[0] == error
