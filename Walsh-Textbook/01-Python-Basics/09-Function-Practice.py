## Lesson 9: Function Practice
# Here are some more exercises for you to practice functions.

## Exercise 1: Fahrenheit Calculator
# In 2018, there was a heat wave in Scotland and Northern Ireland. Temperatures rose above 30 degrees Celsius. You want to know...is that a lot?
# To convert Celsius to Fahrenheit, you mutliply the Celsius temperature by 9/5 and then add 32.
# Create a function called make_fahrenheit() that will take any temperature in Celsius and return the converted temperature in Fahrenheit.
celsius = 30

def make_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  print(fahrenheit)
  
make_fahrenheit(15)

# A few weeks ago, the UK experienced a cold snap. Temperatures plummeted to -8 degrees Celsius. You want to know: uhhh, is that a little?
make_fahrenheit(-8)

## Exercise 2: Is it Warm Outside?
# Let's make a new function is_it_warm() that builds on our make_fahrenheit() function. This function will convert Celsius to Fahrenehit but it will also print out a statement about whether it is warm outside.
# Of course, what one person thinks is warm will be different from what another person thinks is warm. So this function will take in 2 arguments: the temperature in Celsius and the threshold for what is considered a warm temperature.
threshold = 50 # To set one specific threshold.

def is_it_warm(celsius, threshold):
  fahrenheit = (celsius * 9/5) + 32
  if (fahrenheit >= threshold):
    print(f"The temperature is {fahrenheit}°F, so it's warm!")
  else:
    print(f"The temperature is {fahrenheit}°F. Not that warm!")
    
# Try it out with multiple temperatures!
is_it_warm(celsius = 10, threshold = 50)
is_it_warm(celsius = 0, threshold = 50)

## Exercise 3: Chinese Zodiac
# Create a function called chinese_zodiac() that takes in people's birth years and report their corresponding Chinese zodiac sign.
# Make sure you run this cell below! It establishes the list of eligible years.
rat_years = [1924, 1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020, 2032]
ox_years = [1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021, 2033]
tiger_years = [1926, 1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022, 2034]
rabbit_years = [1927, 1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023, 2035]
dragon_years = [1928, 1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024, 2036]
snake_years = [1929, 1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025, 2037]
horse_years = [1930, 1942, 1954, 1966, 1978, 1990, 2002, 2014, 2026, 2038] # This one had an error in the textbook, so I changed it here.
sheep_years = [1931, 1943, 1955, 1967, 1979, 1991, 2003, 2015, 2027, 2039]
monkey_years = [1932, 1944, 1956, 1968, 1980, 1992, 2004, 2016, 2028, 2040]
rooster_years = [1933, 1945, 1957, 1969, 1981, 1993, 2005, 2017, 2029, 2041]
dog_years = [1934, 1946, 1958, 1970, 1982, 1994, 2006, 2018, 2030, 2042]
pig_years = [1935, 1947, 1959, 1971, 1983, 1995, 2007, 2019, 2031, 2043]

# Create the function:
def chinese_zodiac(year):
  if year in rat_years:
    print("🐀 You were born in the Year of the Rat! 🐀")
  elif year in ox_years:
    print("🐂 You were born in the Year of the Ox! 🐂")
  elif year in tiger_years:
    print("🐅 You were born in the Year of the Tiger! 🐅")
  elif year in rabbit_years:
    print("🐇 You were born in the Year of the Rabbit! 🐇")
  elif year in dragon_years:
    print("🐉 You were born in the Year of the Dragon! 🐉")
  elif year in snake_years:
    print("🐍 You were born in the Year of the Snake! 🐍")
  elif year in horse_years:
    print("🐎 You were born in the Year of the Horse! 🐎")
  elif year in sheep_years:
    print("🐏 You were born in the Year of the Sheep! 🐏")
  elif year in monkey_years:
    print("🐒 You were born in the Year of the Monkey! 🐒")
  elif year in rooster_years:
    print("🐓 You were born in the Year of the Rooster! 🐓")
  elif year in doge_years:
    print("🐕 You were born in the Year of the Dog! 🐕")
  else:
    print("🐖 You were born in the Year of the Pig! 🐖")
    
# Try calling the function with your birth year, and another year!
chinese_zodiac(2000)
chinese_zodiac(1967)
