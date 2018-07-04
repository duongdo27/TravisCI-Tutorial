def check_pythagorean(a, b, c):
    """
    :param a:
    :param b:
    :param c:
    :return: Check if the number a, b, c satisfy Pythagorean theorem
    a^2 + b^2 = c^2, a^2 + c^2 = b^2, a^2 = b^2 + c^2
    """
    return a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or a**2 == b**2 + c**2
