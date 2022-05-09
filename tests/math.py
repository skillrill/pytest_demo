import pytest

# setup
# teardown

@pytest.mark.smoke
def test_multiply():
    assert 4*4 == 16

@pytest.mark.smoke
def test_new():
    assert 1==2

@pytest.mark.smoke
def test_new2():
    assert 2==2

@pytest.mark.regression
def test_addition():
    assert 4 + 5 == 9

@pytest.mark.regression
def test_subtract():
    assert 4 - 4 == 0

@pytest.mark.parametrize("x, y", [(4, 16), (5, 25), (1, 5)])
def test_calculate_sqr(x, y):
    assert x * x == y


