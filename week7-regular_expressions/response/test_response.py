from response import validate_mail


def test_default():
    assert validate_mail("malan@harvard.edu") == True
    assert validate_mail("example@mail.com") == True
    assert validate_mail("simple@example.com") == True
    assert validate_mail("Romina@ymail.com") == True
    assert validate_mail("fred&barny@example.net") == True



def test_incorrect():
    assert validate_mail("malan@@@harvard.edu") == False
    assert validate_mail("malan.harvard.edu") == False
    assert validate_mail("malan.edu") == False
    assert validate_mail("malan@harvard..edu") == False
    assert validate_mail("malan@harvard") == False
    assert validate_mail("malan@harvard.") == False
    assert validate_mail("malan") == False
    assert validate_mail("malan@.edu") == False
    assert validate_mail("john.. doe@gmail.com") == False
    assert validate_mail("janedoe@gmail,com") == False
    assert validate_mail("fred\\barny@example.com") == False
