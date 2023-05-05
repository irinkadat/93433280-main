from twttr import shorten


def test_shorten():
    assert shorten('irinka') == 'rnk'
    assert shorten('ir1nka') == 'r1nk'
    assert shorten('IRINKA') == 'RNK'
    assert shorten('IRI NKA.') == 'R NK.'
