## Lesson 7: Dictionaries
# A dictionary is a data type in Python that is used to store data values in pairs, specifically known as key-value pairs.

## Key-Value Pairs
# Key-value pairs are separated by a colon and from other pairs by a comma.
# A dictionary is always enclosed by curly brackets {}.

# Here is an example key-value pair:
prof_walsh = {"name": "Melanie Walsh", "age": 30, "occupation": "Teacher"}
print(prof_walsh)

# You can check all the keys in a dictionary with the .keys() extension, or all the values in a dictionary with the .values() extension.
# Try it out by assigning them to a variable and then printing them!
walsh_categories = prof_walsh.keys()
print(walsh_categories)

walsh_info = prof_walsh.values()
print(walsh_info)

## Accessing Items:
# You can access a value in a dictionary using square brackets [] and its key name, similar to how you index strings or list items.
# Try it out by making your own dictionary about yourself and calling each key!
joe = {"name": "Joe Lollo", "age": 22, "occupation": "Student"}
joe["name"]
joe["age"]
joe["occupation"]

## Changing Items:
# You can also change a value in a dictionary by re-assigninga new value to the key, using the calling syntax from above and the assignment operator.
# Try it out! Change one of your values!
joe["age"] = 100
print(joe)

## Looping Through Items:
# You can also loop through items with a for loop. The .items() extension can show you what each item is.
# Try creating a for loop that prints each item in your dictionary, and another that prints them in a more readable way.
print(joe.items())

# for loop begins here:
for item in joe.items():
  print(item)
  
# for loop with more readable format, using printf (I assume).
for key, value in joe.items():
  print(f"Joe's {key}: {value}")
