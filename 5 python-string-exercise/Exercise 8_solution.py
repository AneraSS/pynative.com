# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
#
# Write a program to find all occurrences of “USA” in a given string ignoring the case.

str1 = "Welcome to USA. usa awesome, isn't it?"
sub_string = "USA"

# convert string to lowercase
temp_str = str1.lower()

# use count function
count = temp_str.count(sub_string.lower())
print("The USA count is:", count)