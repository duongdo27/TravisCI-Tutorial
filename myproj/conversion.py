def convert_celsius_to_fahrenheit(celsius):
    """
    :param celsius: temperature in celcius
    :return temperature in fahrenheit
    """
    if celsius is None:
        return
    return celsius * 1.8 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    """
    :param fahrenheit: temperature in fahrenheit
    :return temperature in celsius
    """
    if fahrenheit is None:
        return
    return (fahrenheit - 32) / 1.8
