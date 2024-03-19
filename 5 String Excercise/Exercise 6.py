# Exercise 5: Create a mixed String using the following rules

# Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last
# char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of
# the result.

str1 = "Abc"
str2 = "Xyz"
#AzbycX

str3 = ""

# reverse str2
str2_rev = str2[::-1]

# get minimum length between strings
min_len = min(len(str1), len(str2_rev))

# join the strings
for i in range(min_len):
    str3 = str3 + str1[i] + str2[i]

# join remaining characters, if the strings are not of same length
str3 = str3 + str1[min_len:] + str2[min_len:]

print(str3)