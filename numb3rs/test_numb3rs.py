from numb3rs import validate

def test_valid_ipv4():
    assert validate('192.168.0.1') == True
    assert validate('10.0.0.1') == True
    assert validate('132.8.0.1') == True
    assert validate('255.255.255.0') == True

def test_invalid_ipv4():
    assert validate('256.128.0.1') == False
    assert validate("512.512.512.512") == False
    assert validate('a.b.c.d') == False
    assert validate('1.2.3.4.5') == False
    assert validate('1,2,3,4') == False
