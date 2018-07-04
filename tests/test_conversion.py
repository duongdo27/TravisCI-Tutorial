from myproj.conversion import convert_celsius_to_fahrenheit


def test_celsius_to_fahrenheit():
    assert convert_celsius_to_fahrenheit(0) == 32
    assert convert_celsius_to_fahrenheit(100) == 212


def test_celsius_to_fahrenheit_none():
    assert convert_celsius_to_fahrenheit(None) is None
