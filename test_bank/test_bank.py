from bank import value

def test_start_hello():
    assert value('hello iri') == 0

def test_h():
    assert value('Heyy there') == 20

def test_other():
    assert value('bonjuorno') == 100