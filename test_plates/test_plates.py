from plates import is_valid


def test_is_valid():
    assert is_valid("AB123")
    assert not is_valid("GHIok789")
    assert not is_valid("10jkk")
    assert not is_valid("M")
    assert not is_valid("44")
    assert not is_valid("QR02")
    assert not is_valid("33kkd")
    assert not is_valid("kkd22d")
    assert not is_valid("he3!1")

