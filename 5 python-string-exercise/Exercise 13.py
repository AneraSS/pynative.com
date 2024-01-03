# Exercise 13: Split a string on hyphens
#
# Write a program to split a given string on hyphens and display each substring.

str1 = "Emma-is-a-data-scientist"
# Displaying each substring
#
# Emma
# is
# a
# data
# scientist

substrings = str1.split("-")

for substring in substrings:
    print(substring)