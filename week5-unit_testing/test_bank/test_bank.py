from bank import value


def test_default():
    assert value("hello") == 0
    assert value("   hello   ") == 0
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0


def test_start_with_h():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("H") == 20
    assert value("How you doing?") == 20
    assert value("How is it going?") == 20


def test_starts_without_h():
    assert value("") == 100
    assert value("What's happening?") == 100
    assert value("What's up?") == 100
    assert value("oh, hello. may I help you?") == 100
    assert value("oh, hi") == 100