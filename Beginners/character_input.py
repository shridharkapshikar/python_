#Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
#

name = input("Please enter your name: ")
age = input("Please enter your birth year: ")
age = int(age)

after_100 = age + 100

print("%d will be a year you turn 100 years"%after_100)