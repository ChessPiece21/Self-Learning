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
