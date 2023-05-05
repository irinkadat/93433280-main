import pytest
from seasons import calculate_minutes


def test_one_year_ago():
    assert calculate_minutes("2022-04-29") ==  "Five hundred twenty-eight thousand, four hundred eighty minutes"
def test_two_years_ago():
    assert calculate_minutes("2021-04-29") ==  "One million, fifty-four thousand eighty minutes"


def test_invalid_date():
    with pytest.raises(ValueError):
        calculate_minutes("January 1, 1999")


if __name__ == "__main__":
    unittest.main()














