from plates import is_valid

def test_default():
    assert is_valid("CS50") == True
    assert is_valid("SAMPLE") == True
    assert is_valid("AAA222") == True


def test_no_input():
    assert is_valid("") == False


def test_invalid_start():
    assert is_valid("C123") == False
    assert is_valid("12csd") == False


def test_len_plate():
    assert is_valid("OUTATIME") == False
    assert is_valid("H") == False
    assert is_valid("ABC123") == True
    assert is_valid("CS") == True


def test_middle_number():
    assert is_valid("CS50P") == False
    assert is_valid("AA0") == False
    assert is_valid("AB123C") == False


def test_first_number_zaro():
    assert is_valid("CS05") == False
    assert is_valid("CS000") == False


def test_punctuations():
    assert is_valid("CS?50!") == False
    assert is_valid("PI3.14") == False