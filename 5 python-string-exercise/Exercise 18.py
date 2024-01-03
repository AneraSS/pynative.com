# Exercise 18: Replace each special symbol with # in the following string

str1 = '/*Jon is @developer & musician!!'
# output: ##Jon is #developer # musician##

new_string = ""
for char in str1:
    if char.isalpha():
        new_string = new_string + char
    elif char == " ":
        new_string = new_string + " "
    else:
        new_string = new_string + "#"

print(new_string)