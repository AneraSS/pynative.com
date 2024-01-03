# Exercise 12: Find the last position of a given substring
#
# Write a program to find the last position of a substring “Emma” in a given string.

str1 = "Emma is a data scientist who knows Python. Emma works at google."
# Last occurrence of Emma starts at index 43

last_occurance = str1.rfind("Emma")

print(f"Last occurrence of Emma starts at index {last_occurance}")