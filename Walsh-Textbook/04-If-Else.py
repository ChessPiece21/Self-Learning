## Lesson 3: Comparisons and Conditionals
# Writing Python code is a lot like writing a list of detailed instructions to the computer. Most of the time you will be asking the computer to perform certain tasks if certain conditions are met. 
# For example: if a person in the dataset is older than 30, print that.
# Here's how we would write that in Python code.
# if age > 30:
  # print("This person is older than 30.")
  
## Comparisons:
# There are many ways that we can compare values with Python, such as equals (==), not equals (!=), greater than (>), less than (<), greater than or equal to (>=), or less than or equal to (<=).
# We can also combine values and compare them. We can check to see if x and y are both True or if either x or y is True.
# This is done through Boolean operators (and, or, and not).

# What will happen if we check whether two people's ages are older or younger than 30!
# Assign the variables age1 and age2, one above 30.
age1 = 30
age2 = 35
# Write Boolean expressions for age1 and age2 being greater than 30, using and and or.
age1 > 30 and age2 > 30
age1 > 30 or age2 > 30
# Write a Boolean expression using the greater than or equal to sign.
age1 >=0 and age2 >= 30
# This one is true, because age1 is equal to 30 while age2 is greater than 30. The and Boolean requires that both conditions are true.

## Conditionals: if and else
# An if statement is an instruction for something IF a particular condition is met. A common if statement will consist of two lines:
 # On the first line, you type the English word if followed by an expression and then a colon (:)
 # On the second line, you indent and write an instruction or "statement" to be completed if the condition is met
# You can add more complexity by adding an else statement after, which should be formatted in the same way.

# Try it out using this variable!
beyonce = "award winner"

# Write an if statement that prints "Congratulations, Beyonce!" if award winner is true, and an else statement for all other conditions. Be creative with the response!
if beyonce == "award winner":
  print("Congratulations, Beyonce!")
else:
  print("They done messed up...")

## elif Statements:
# Sometimes you want even more nuance to respond to slightly different conditions. For example, if Beyonce was nominated for a Grammy but didn't win, then we might want to express a slightly different sentiment than if she won or was not nominated at all.
# You can add this withan elif (else if in other programming languages) statement, which is placed between the if and else.
# Integrate an elif statement below, after changing the beyonce variable to "award nominee":
beyonce = "award nominee"

if beyonce == "award winner":
  print("Congratulations, Beyonce!")
elif beyonce == "award nominee":
  print("Ok, well at least they nominated you...")
else:
  print("They done messed up...")
