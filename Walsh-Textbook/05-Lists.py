## Lesson 5: Lists and Loops
## Lists:
# A list is a Python data structure, a way of grouping multiple values together. We've already encountered lists with the .split() method!

# Create a variable of the same Kafka intro from the first assignment, and use the .split() method to create a list.
kafka_intro = "One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin."
kafka_list = kafka_intro.split()
print(kafka_list)

# A list is always enclosed by square brackets [] and accepts items in a row separated by commas.
# Lists can contain any combination of Python data types — strings, numbers, or booleans all mixed together.
# Create a list of 5 different names, numbers, and combined variables.
names = ["John", "Mary", "Peter", "Thomas", "Claire"]
numbers = [28, 16, 59, 80, 33]
combined = ["I", "want", 50, "tacos"]

# Check that they're lists using the type() function.
type(names)
type(ages)
type(combined)

# To identify and print a specific list item, you need to use the square brackets [] after the list name, with the index you want to select the item from inside the bracket.
# Try this out with the first variable, and remember what they start with!
names[0]

# You can also reassign variables using this same method. Reassign the first number to a second number of your choice, and print it.
numbers[0] = 99
numbers

## Sorting
# To sort items in a list, you use the .sort() extension. By default, it's done in ascending order.
sorted_numbers = numbers.sort()
print(sorted_numbers)

# Descending order requires reverse=True in the parentheses. As we learned last lesson, this is a Boolean expression.
# Try sorting them now!
sorted_numbers = numbers.sort(reverse=True)
print(sorted_numbers)

## Other Methods:
## Appending
# Using the .append() extension, you can add values to a list. Try it out with the list and value of your choice.
names.append("Joe")
print(names)

## Length:
# Using the function len(), you can calculate the length of a list.
# Try this out with the list you appended to.
len(names)

## Extra Method:
## Enumerating:
# You might want to keep a numerical count or index of items in a list. To print out each item in the list with a corresponding number, you can use the built-in Python function enumerate().
# This is a for loop, which will be discussed in the next lesson.
for count, name in enumerate(names):
  print(count, name)
