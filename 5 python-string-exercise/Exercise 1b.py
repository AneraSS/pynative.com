# Exercise 1B: Create a string made of the middle three characters
# Write a program to create a new string made of the middle three characters of an input string.

string1 = 'JhonDipPeta'
string2 = 'JaSonAy'


def get_middle(string):
    middle2 = string[int(len(string)/2)]
    middle1 = string[int(len(string)/2)-1]
    middle3 = string[int(len(string)/2)+1]
    print (middle1+middle2+middle3)

get_middle('JhonDipPeta')
get_middle('JaSonAy')