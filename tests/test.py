from datetime import datetime
import pytest

from ddbot.logic import Pregnancy


@pytest.mark.parametrize("last_period, expected_due", [
    (datetime(2010, 9, 9), datetime(2011, 6, 16)),
    (datetime(2022, 4, 12), datetime(2023, 1, 17)),
    ("2022-04-12", datetime(2023, 1, 17))
])
def test_due_01(last_period, expected_due):
    assert Pregnancy.from_last_menstrual_cycle(last_period).due_date == expected_due


@pytest.mark.parametrize("c_date, expected_due", [
    (datetime(2023, 1, 6), datetime(2023, 9, 29)),
    (datetime(2022, 4, 6), datetime(2022, 12, 28)),
    ("2022-04-06", datetime(2022, 12, 28))
])
def test_due_02(c_date, expected_due):
    assert Pregnancy.from_conception_date(c_date).due_date == expected_due
