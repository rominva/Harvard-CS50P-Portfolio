from twttr import shorten

def test_default():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Romina") == "Rmn"


def test_no_vowels():
    assert shorten("CS") == "CS"
    

def test_alphanumeric():
    assert shorten("CS50") == "CS50"


def test_no_input():
    assert shorten("") == ""


def test_numbers():
    assert shorten("50") == "50"


def test_just_vowels():
    assert shorten("AEIOU") == ""
    assert shorten("aeiou") == ""


def test_punctuations():
    assert shorten("What's your name?") == "Wht's yr nm?"


