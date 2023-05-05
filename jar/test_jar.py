import pytest
from jar import Jar

def test_init():
    jar = Jar()
    jar.capacity == 12
    jar.size == 0
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar('str')

def test_str():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size==2


    assert (jar.deposit(4), jar.size) == (None, 6)


def test_invalid_depo():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit('jdjf')


def test_withdraw():
    jar = Jar(4)
    jar.deposit(2)
    jar.withdraw(1)
    assert jar.size == 1

    with pytest.raises(ValueError, match="there's no enough cookies!"):
        jar.withdraw(3)


