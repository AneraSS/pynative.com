# Exercise 1A: Create a string made of the first, middle and last character
# Write a program to create a new string made of an input string’s first, middle, and last character.

string = 'James'
first = string[0]
middle=string[int(len(string)/2)] # must be integer
last = string[-1]

new_string=first+middle+last
print(new_string)