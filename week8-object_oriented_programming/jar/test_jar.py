from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12

    jar2 = Jar(20)
    assert jar2.capacity == 20

    jar3 = Jar(0)
    assert jar3.capacity == 0

    with pytest.raises(ValueError):
        Jar(4.5)

    with pytest.raises(ValueError):
        Jar(-5) 


def test_str():
    jar = Jar()
    assert str(jar) == ""
    
    jar.deposit(1)
    assert str(jar) == "🍪"
    
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪🍪"

    jar.withdraw(2)
    assert str(jar) == "🍪🍪🍪"

    jar.withdraw(3)
    assert str(jar) == ""


def test_deposit():
    jar = Jar(10)

    jar.deposit(5)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.deposit(6)

    assert jar.size == 5

    jar2 = Jar(20)
    jar2.deposit(20)
    assert jar2.size == 20
    

def test_withdraw():
    jar = Jar(9)

    jar.deposit(9)
    jar.withdraw(5)
    assert jar.size == 4

    with pytest.raises(ValueError):
        jar.withdraw(6)

    assert jar.size == 4

    jar.withdraw(4)
    assert jar.size == 0