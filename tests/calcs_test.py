import pytest
from app.calcs import add, div
# Run cmd: pytest -v -s in terminal from root directory
# -v for verbose, -s for showing print statements.


@pytest.mark.parametrize("num1, num2, expected", [(5, 5, 10), (3, 3, 6), (7, 2, 9)])
def test_add(num1, num2, expected):
    sum = add(num1, num2)
    assert sum == expected


@pytest.mark.parametrize("num1, num2, expected", [(10, 0, 1)])
def test_div(num1, num2, expected):
    with pytest.raises(ZeroDivisionError):
        answer = div(num1, num2)
        assert answer == expected
