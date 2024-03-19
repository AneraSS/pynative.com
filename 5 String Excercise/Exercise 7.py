# Exercise 7: String characters balance Test
#
# Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the
# characters in the s1 are present in s2. The character’s position doesn’t matter.

#s1 = "Yn"
#s2 = "PYnative"
#True

s1 = "Ynf"
s2 = "PYnative"
# False

if s1 in s2:
    print(True)
else:
    print(False)