## Lesson 2: String Methods
# A string is a Python data type that is treated like text, even if it contains a number. Strings are always enclosed by either single quotation marks 'this is a string' or double quotation marks "this is a string". In this lesson, we're going to explore some special things that you can do with strings.

## Practice with Strings
# Use the introduction from Franz Kafka's Metamorphosis from the class/textbook repository.
# Open the text using the open() method, save to a string variable named sample_text.
sample_text = open("intro.txt")

# Check that it's a string and print it.
type(sample_text)
print(sample_text)

## Indexing and Extracting Strings
# By using square brackets [], you can grab or "index" part of a string based on its character number.
# A Python index begins with 0. Place the 0 in a 
sample_text[0]

## Slicing Strings
# You can also slice between characters or up to certain characters, using this syntax:
# string[start:stop:step]
# By putting specific index numbers between these colons, you can slice the string at certain starting and stopping points, and you can also "step" by different amounts—that is, you can jump by a certain number through the string and take every nth item in the string (e.g. every 3rd item).
# Let's index our Kafka sample text from the beginning to the 121st character.
sample_text[0:121]
# Alternatively, 
sample_text[:121]

# Now, index from the 121st to 250th.
sample_text[121:250]

# Let's create a variable, first_line, and assign it to the first sentence of The Metamorphosis.
first_line = sample_text[:121]
print(first_line)

## Replacing Words:
# To replace a certain string within another string, you can use the replace method, which uses this syntax:
# string.replace('old string', 'new string')

# Replace "vermin" with the horrible subject of your choice!
new_first_line = first_line.replace("vermin", "Soundcloud rapper")
print(new_first_line)

## Transforming to Upper and Lowercase Letters:
# You can also replace the text in strings to upper-, lower-, and title-case, using the .lower(), .upper(), and .title()
new_first_line.upper()
new_first_line.lower()
new_first_line.title()

## Splitting Strings:
# With the .split() method, you can split up a strings into a a list of parts. By default, it splits on spaces, but you can put in a different delimiter and split on something else.
# string.split('delim')
# Try this out with your new first line!
new_first_line.split()

# Create a variable called split_words, using this method.
split_words = new_first_line.split()
print(split_words)

## Strip and Split:
# You can also easily strip white space from the beginning and end of a string using .split().
# Try it out on this variable of the Kafka passage!
dirty_kafka = " One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin. \t"
print(dirty_kafka)

dirty_kafka.strip()

# What's interesting about Python is that you can also chain methods together in a single line, try running it here with .strip() and .split!
dirty_kafka.strip().split()

## Joining Strings by a Delimiter
# The opposite of .split() is .join(), which joins the elements in a given list together using a string.
# Try it out with a sentence of your choice!
sentence = "Hey guys, did you know that in terms of male human and female Pokémon breeding, Vaporeon is the most compatible Pokémon for humans?"
split_sentence = sentence.split()
split_sentence

" ".join(split_sentence)
