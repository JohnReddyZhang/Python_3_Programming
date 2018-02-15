def convert_temperatures(key, *args):
    templist = [*args]
    if key == 'Celsius':
        return celsius_to_fahrenheit(templist)
    elif key == 'Fahrenheit':
        return fahrenheit_to_celsius(templist)
    else:
        print('Wrong Unit!')


def celsius_to_fahrenheit(templist):
    converted = [float(temp) * 1.8000 + 32.000 for temp in templist]
    return converted


def fahrenheit_to_celsius(templist):
    converted = map(lambda temp: (float(temp)-32)/1.8000,templist)
    return converted

# Information source: http://www.metric-conversions.org/temperature/fahrenheit-to-celsius.htm
