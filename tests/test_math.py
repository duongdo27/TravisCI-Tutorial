from myproj.math import check_pythagorean


def test_check_pythagorean():
    assert check_pythagorean(3, 4, 5) is True
    assert check_pythagorean(3, 5, 4) is True
    assert check_pythagorean(5, 3, 4) is True
