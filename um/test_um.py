from um import count

def test_question_mark():
    assert count("um?") == 1

def test_case_insensitive():
    assert count("Um, thanks for the album.") == 1

def test_multiple_um():
    assert count("Um, thanks, um...") == 2


