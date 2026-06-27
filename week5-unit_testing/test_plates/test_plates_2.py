from plates import is_valid

def test_default():
    assert is_valid("CS50")
    assert is_valid("SAMPLE")
    assert is_valid("AAA222")


def test_no_input():
    assert not is_valid("")


def test_invalid_start():
    assert not is_valid("C123")
    assert not is_valid("12csd")


def test_len_plate():
    assert not is_valid("OUTATIME")
    assert not is_valid("H")
    assert is_valid("ABC123")
    assert is_valid("CS")


def test_middle_number():
    assert not is_valid("CS50P")
    assert not is_valid("AA0")
    assert not is_valid("AB123C")


def test_first_number_zaro():
    assert not is_valid("CS05")
    assert not is_valid("CS000")


def test_punctuations():
    assert not is_valid("CS?50!")
    assert not is_valid("PI3.14")