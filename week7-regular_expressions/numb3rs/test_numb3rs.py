from numb3rs import validate


def test_default():
    assert validate("127.0.0.1") == True


def test_edges():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("256.0.0.0") == False


def test_outofrange():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("-2.-6.-5.-200") == False


def test_leading_zeros():
    assert validate("192.168.001.1") == False
    assert validate("01.02.03.04") == False
    assert validate("00.0.0.0") == False


def test_invalid_format():
    assert validate("cat") == False
    assert validate("25-125-255-50") == False
    assert validate("200/100/89/90") == False
    assert validate("1. 2. 3. 4") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
