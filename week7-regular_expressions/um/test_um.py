from um import count

def test_defult():
    assert count("um") == 1
    assert count(" um ") == 1
    assert count("hello, um, world") == 1
    assert count("um?") == 1
    assert count("um, thanks for the um...album.") == 2
    assert count("um um um um") == 4

def test_substring():
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("Drum") == 0


def test_case_insensitively():
    assert count("UM") == 1
    assert count("Was your name Um...Romi or uM...somthing else?") == 2
    assert count("UM, um, Um, uM") == 4


def test_space():
    assert count("u m") == 0
