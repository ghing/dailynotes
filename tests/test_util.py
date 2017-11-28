from datetime import date, timedelta

import dailynotes.util


# Wednesday, November 22, 2017
base_date = date(2017, 11, 22)


def test_get_date_empty():
    d = dailynotes.util.get_date('', base_date)
    assert d == base_date


def test_get_date_today():
    d = dailynotes.util.get_date('today', base_date)
    assert d == base_date


def test_get_date_yesterday():
    d = dailynotes.util.get_date('yesterday', base_date)
    assert d == base_date - timedelta(days=1)


def test_get_date_tomorrow():
    d = dailynotes.util.get_date('tomorrow', base_date)
    assert d == base_date + timedelta(days=1)


def test_get_date_sunday():
    d = dailynotes.util.get_date('sunday', base_date)
    assert d == date(2017, 11, 19)


def test_get_date_monday():
    d = dailynotes.util.get_date('monday', base_date)
    assert d == date(2017, 11, 20)


def test_get_date_tuesday():
    d = dailynotes.util.get_date('tuesday', base_date)
    assert d == date(2017, 11, 21)


def test_get_date_wednesday():
    d = dailynotes.util.get_date('wednesday', base_date)
    assert d == date(2017, 11, 15)


def test_get_date_thursday():
    d = dailynotes.util.get_date('thursday', base_date)
    assert d == date(2017, 11, 16)


def test_get_date_friday():
    d = dailynotes.util.get_date('friday', base_date)
    assert d == date(2017, 11, 17)


def test_get_date_saturday():
    d = dailynotes.util.get_date('saturday', base_date)
    assert d == date(2017, 11, 18)
