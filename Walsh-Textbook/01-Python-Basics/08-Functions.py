## Lesson 8: Functions
# A function is way of bundling up code to perform specific tasks. It's kind of like making a little Python wind-up toy that runs on command.
# We've encountered built-in functions in Python many times already, including print(), len(), and type().

## Defining functions.
# To make your own function, you use the keyword def, short for define, followed by your desired name for the function, parentheses (()) and a colon (:).
# Finally, you complete the function with a return statement.
# To try this out, create a function called sing(), where the content is that it prints the opening line to a song you like.
def sing():
  print(f"🎵SOME-body once told me...🎵")
  
## Calling Functions:
# To call a function you simply type the name of the function in parentheses.
sing()

## Editing Functions:
# You can also place things in the input parentheses, when variables are assigned, to change the output.
# Try it out as indicated in the textbook with your own name!
def say_happy_birthday(name = "Joe"):
  print(f"Happy birthday, {name}! Here's to another great year!")

# Now call the function with other names!
say_happy_birthday("Beyonce")
say_happy_birthday("Jesus")
say_happy_birthday("Kanye")
  
## Regular Expressions
# The regular expressions module, imported as re, will allow you to use regular expressions — a special pattern-matching language that allows you to do sophisticated find-and-replace and text manipulation. 
# We will discuss regular expressions more in the coming weeks. For now, just edit the sample string with the word of your choice.
sample_string = "I'm the giant rat that makes all of the rules."
import re
re.split('\W+', sample_string)
  
# Create a function called split_words and integrate the regular expression to split words in it.
def split_words(text):
  split_words = re.split('\W+', text)
  return split_words
  
# Try calling split_words to to split "The Pool Players: Seven at the Golden Shovel" by Gwendolyn Brooks (written out here) into individual words.
poem = "We real cool. We left school. We lurk late. We strike straight. We sing sin. We thin gin. We Jazz June. We die soon."
split_words(poem)

# Let's see if this is different than what happens when words are tokenized.
tokenized_poem = split_words(poem)
print(tokenized_poem)

## Return Values:
# In all of the examples above, we weren’t returning any specific value, just using print() statements. But sometimes you want a specific value out of your function. For example, if we want to make a function that transforms a bit of text into very loud-sounding text, then we’ll want to return that loud-sounding text.
# Make the shouty text, as indicated in the textbook.
def make_text_shouty(text):
  shouty_text = text.upper()
  return shouty_text

# Do the same thing, but call it make_text_whispery that transforms it to lowercase.
def make_text_whispery(text):
  whispery_text = text.lower()
  return whispery_text

make_text_whispery("I LOVE TACOS")
