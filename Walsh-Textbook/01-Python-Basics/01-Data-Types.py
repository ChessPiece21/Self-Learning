## Lesson 1: Python Data Types
# In this lesson, we're going to explore Python variables and data types.
# Variables are one of the fundamental building blocks of Python. A variable is like a tiny container where you store values and data, such as filenames, words, numbers, collections of words and numbers, and more.
# - Strings are text, written between quotes "" or ''.
# - Integers are whole numbers.
# - Floats are decimal numbers.
# - Boolean are True/False values.

# While we're learning these Python basics, let's pretend that we're going to build a program to determine the ideal office temperature. We will establish the current office temperature and then report whether that temperature is too hot, too cold, or ideal.
print("We are going to calculate the ideal office temperature for everyone.")

## Variable Assignment:
# Let's first establish the current temperature of our imagined office: 71 degrees. How can we assign the value 71 to the office_temperature?
office_temperature = 73

## Checking Data Types:
# What type of Pythondata is office_temperature?
type(office_temperature)

## Display Variables:
# We can display variables in two different ways with Jupyter notebooks. Are there differences?
print(office_temperature)
office_temperature
# There's no difference! These methods are the same.

## Python Expressions:
# This is a Python expression. What do you guess is the resulting value?
office_temperature + 3
#print(office_temperature + 3) # Alternatively.

office_temperature - 2
#print(office_temperature - 2)

## Variable Re-Assignment:
# Re-assign office temperature to a new value.
office_temperature = 72
# Print the variable to see if it changed.
office_temperature

## Boolean Values
# Let's create some Boolean values that will report whether it's too warm, too cold, or the ideal office temperature.
too_warm = office_temperature > 73
too_warm

too_cold = office_temperature < 70
too_cold

ideal_temp = office_temperature == 72
ideal_temp
# Check the type after testing.
type(ideal_temp)

## F-Strings (Formatted Strings)
# A special kind of string that we're going to use in this class is called an f-string. An f-string, short for formatted string literal, allows you to insert a variable directly into a string.
# An f-string must begin with an f outside the quotation marks. Then, inside the quotation marks, the inserted variable must be placed within curly brackets {}.
print(f"The office temperature is {office temperature}. Thus, it is {ideal_temp} that the office is in the ideal temperature." 

