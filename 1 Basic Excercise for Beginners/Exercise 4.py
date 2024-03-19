# Write a program to remove characters from a string starting from zero up to n and return a new string.

# word = input ("Please enter the word: ")
# number = input("Please enter number: ")
# number= int(number)

def remove_chars(word, number):
    return (word[number:])

print(remove_chars('pynative',4))
print(remove_chars('pynative', 3))
print(remove_chars('martin', -1))