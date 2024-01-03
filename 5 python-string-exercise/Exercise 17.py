# Exercise 17: Find words with both alphabets and numbers
#
# Write a program to find words with both alphabets and numbers from an input string.

str1 = "Emma25 is Data scientist50 and AI Expert"
# Emma25
# scientist50

items = str1.split(" ")
print(items)

for item in items:
    if item[0].isalpha() and item[-1].isdigit():
        print(item)

############
def hasDigit(word):
    for char in word:
        if char.isdigit():
            return True
    return False

def hasAlpha(word):
    for char in word:
        if char.isalpha():
            return True
    return False

print("\nBetter solution:")
words = str1.split(" ")
for word in words:
    if hasDigit(word) and hasAlpha(word):
        print(word)


