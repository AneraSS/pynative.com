# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
#
# Write a program to find all occurrences of “USA” in a given string ignoring the case.

str1 = "Welcome to USA. usa awesome, isn't it?"
# The USA count is: 2

# transform string into a list split by whitespace " "
str1_list = str1.split()

# change all present USA combinations to "usa" (lowercase)
my_list = []
for item in str1_list:
    my_list.append(item.lower())

# remove special characters that may be next to "usa", eg. "usa." --> "usa"; such as ., !, ?
characters_to_remove = "!.?"
cleaned_list = []
for word in my_list:
    for char in characters_to_remove:
        word = word.replace(char, "")
    cleaned_list.append(word)

print (cleaned_list)

#this works only for one character removal, otherwise duplicates due to append are created
#for word in new_list:
#    cleaned_list.append(word.strip("."))

# count number of occurrences
count = 0
for word in cleaned_list:
    if word == "usa":
        count+= 1

print(f"Number of occurrences: {count}")