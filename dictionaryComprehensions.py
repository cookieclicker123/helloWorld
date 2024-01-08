#Dictionary comprehensions are similar to list comprehensions, but allow you to easily construct dictionaries. They allow you to create dictionaries using for loops, including conditional statements.

# dictionary  = {key: expression for (key, value) in iterable}

#citiesInF = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
#citiesInC = {key: round((value - 32)*(5/9)) for (key,value) in citiesInF.items()}
#print(citiesInC)


#weather = {'New York': 'snowing', 'Boston': 'sunny', 'Los Angeles': 'sunny', 'Chicago': 'cloudy'}

#sunnyWeather = {key: value for (key,value) in weather.items() if value == "sunny"}
#print(sunnyWeather)


cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

#descCities = {key: ("WARM" if value >= 40 else "COLD") for (key, value) in cities.items()}
#print(descCities)

def checkTemp(value):
    if value >= 70:
        return "HOT"
    elif value >=40:
        return "WARM"
    else:
        return "COLD"

descCities = {key: checkTemp(value) for (key, value) in cities.items()}
print(descCities)