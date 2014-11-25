from webapp import get_result

__author__ = 'Michael Cheah'


def test_result():
    """100 is the correct number in all cases here"""
    assert get_result(100, 100) == "Correct!"
    assert get_result(1, 100) == "Too Low!"
    assert get_result(1000, 100) == "Too High!"