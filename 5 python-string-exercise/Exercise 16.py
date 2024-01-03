# Exercise 16: Removal all characters from a string except integers

str1 = 'I am 25 years and 10 months old'
# 2510

new_string = ""
for char in str1:
    if char.isdigit():
        new_string += char

print(int(new_string))