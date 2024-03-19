# Exercise 15: Remove special symbols / punctuation from a string

str1 = "/*Jon is @developer & musician"
# "Jon is developer musician"

#Use string functions translate() and maketrans().
#The string.punctuation constant contain all special symbols.

import string

str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)

new_str = str1.translate(str.maketrans('', '', string.punctuation))

print("New string is: ", new_str)