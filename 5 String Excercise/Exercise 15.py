# Exercise 15: Remove special symbols / punctuation from a string

str1 = "/*Jon is @developer & musician"
# "Jon is developer musician"

new_string = ""
for char in str1:
    if char.isalpha() or char == " ":
        new_string += char

print(new_string)