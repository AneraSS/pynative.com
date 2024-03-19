# Exercise 10: Write a program to count occurrences of all characters within a string

str1 = "Apple"
#{'A': 1, 'p': 2, 'l': 1, 'e': 1}

# fills dictionary with keys (cahracters from input string)
char_dict = {}
for char in str1:
    char_dict[char] = str1.count(char)

print(char_dict)
