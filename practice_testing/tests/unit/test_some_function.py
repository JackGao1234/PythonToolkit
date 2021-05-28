import pytest

from some_function import capitalize


@pytest.mark.parametrize("input_data, expected",
                         [
                             ("foo", "Foo"),
                             ("a", "A"),
                             ("", ""),
                             ("Bar", "Bar"),
                             (None, None)
                         ]
                         )
def test_capitalize(input_data, expected):
    actual = capitalize(input_data)

    assert actual == expected
