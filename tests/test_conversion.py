from myproj.conversion import convert_celsius_to_fahrenheit
from myproj.conversion import convert_fahrenheit_to_celsius


def test_celsius_to_fahrenheit():
    assert convert_celsius_to_fahrenheit(0) == 32
    assert convert_celsius_to_fahrenheit(100) == 212


def test_celsius_to_fahrenheit_none():
    assert convert_celsius_to_fahrenheit(None) is None


def test_fahrenheit_to_celsius():
    assert convert_fahrenheit_to_celsius(32) == 0
    assert convert_fahrenheit_to_celsius(212) == 100


def test_fahrenheit_to_celsius_none():
    assert convert_fahrenheit_to_celsius(None) is None
