## Lesson 3: Files & Character Encoding
# In this lesson, we're going to explore how to read and write files with the correct character encodings.

# Ask for help with the open() function, to see how it works.
help(open)

## Opening Text Files:
# If you want to read or write a text file with Python, it is necessary to first open the file. To open a file, you can use Python's built-in open() function.
# Open the file that you downloaded from this lesson, taylor_swift_intro.txt, using the guidelines from help(open)!
# Inside the open() function parentheses, you insert the filepath to be opened in quotation marks. You should also insert a character encoding. This function returns what's called a file object.
open('taylor_swift_intro.txt', mode='r', encoding='utf-8')

# It doesn't contain readable text yet, so you need to place the .read() command at the end.
open('taylor_swift_intro.txt', mode='r', encoding='utf-8').read()

## Reading Lines:
# To open a file and read it one by one, you can use the .readlines() method at the end, which you can try out here with taylor_swift.txt, the full lyrics of "State of Grace."
open('taylor_siwft.txt', mode='r', encoding='utf-8').readlines()
# Check the type. It returns a set of lines, which we will talk about in a moment.
type(open('taylor_siwft.txt', mode='r', encoding='utf-8').readlines())

## Assigning Text as Variables:
# Assign the text to a variable using the assignment operator.
tswift = open('taylor_siwft.txt', mode='r', encoding='utf-8').read()
print(tswift)
type(tswift)

## Remix!
# Use the .replace() method to change one line to another, and then add it to a new variable called remix.
remix = tswift.replace("I", "You")
print(remix)

## Writing a Text File:
# The default mode for the open() function is to read text files: mode = 'r'.
# But you can use the open() function to write files, too. Simply set the mode to write: mode = 'w'
# Let's create a new text file with our remixed version of the opening Taylor Swift song.
open('remixed_tsiwft.txt', mode='r', encoding='utf-8').write(remix)
# Double-click on your file in the file browser at the left and see if it worked!

## Character Encoding:
# Why do we need to include encoding='utf-8' to open our text file?
# UTF-8 is a character encoding known as Unicode. We need to specify a character encoding because — gasp! — computers don't actually know what text is. Character encodings are systems that map characters to numbers.
# You can check any characters' "code point," or place in the Unicode universe, with the function ord(
ord("a")
ord("💩")
ord("ত")
ord("!")
