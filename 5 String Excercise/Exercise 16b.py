# Exercise 16: Removal all characters from a string except integers

str1 = 'I am 25 years and 10 months old'
# 2510

str1 = 'I am 25 years and 10 months old'
print("Original string is", str1)

# Retain Numbers in String
# Using list comprehension + join() + isdigit()
res = "".join([item for item in str1 if item.isdigit()])

print(res)