## Lesson 6: More List Methods
# These exercises will help you practice more skills and methods with lists.

## For Loops
# What if we wanted to remove something from a list?
# What if we wanted to calcuate the year each person was born based on their ages?
# One of the best ways to work with these questions in a list is with for loops, as was hinted at in the last lesson.
# This is a way of considering each item in the list or iterating through the list.

# A basic basic for loop will consist of two lines:
# - On the first line, you type the English word for, a new variable name for each item in the list, the English word in, the name of the list, and a colon (:)
# - On the second line, you indent and write an instruction or “statement” to be completed for each item in the list.

# Try it out using some data from the Bellevue Almshouse Dataset: https://gih.hosting.nyu.edu/almshouse/the-almshouse-records/
# Here is the list of the first six names in the dataset. Add a for loop that prints each name with a sentence, like "This person's name is Mary."
first_names = ["Mary", "John", "Anthony", "Margaret", "Unity(?)", "Catherine"]
for name in first_names:
  print(f"This person's name is {name}")

## Creating Lits with for Loops and Nested if Statements:
# You can even create lists with for loops if they have nested if statements in them! Create one here, using the .append() extension to add one to a blank list. 
# Try it out with the M names:
m_names - []

for name in first_names:
  if name.startswith("M"):
    m_names.append(name)
    
print(m_names)

## in and not in:
# You can test whether an item is in a list or not using the keywords in or not in.
fruits = ["apple", "kumquat", "KIWI", "banana", "kiwi", "APPLE", "tomato", "Orange", "orange", "Apple", "pineapple"]
          
# Test in with an if statement:
if "kiwi" in fruits:
  print("A kiwi is totally a fruit.")
  
# We want to make a new list of Disney movies but only if the movies were also contemporary (post-2000s) blockbusters (made a lot of money) called contemp_disney_blockbusters.
# Try to make it from a blank list that features movies in both!
disney_movies = ['Mulan', 'Toy Story', 'Aladdin', 'Monsters Inc.', 'The Lion King', 'Jungle Book', 'Finding Nemo', 'Inside Out', 'Frozen']
contemp_blockbusters = ['Finding Nemo', 'Shrek', 'Monsters Inc.', 'Mission Impossible', 'Harry Potter', 'Wonder Woman', 'Frozen']

# Create the blank list:
contemp_disney_blockbusters = []

for movie in disney_movies:
 if movie in contemp_blockbusters:
  contemp_disney_blockbusters.append(movie)
  
# Print to make sure it worked:
contemp_disney_blockbusters

# Bonus textbook exercise: creating the non-Disney list.
contemp_nondisney = []

for movie not in disney_movies:
  contemp_nondisney.append(movie)

contemp_nondisney
