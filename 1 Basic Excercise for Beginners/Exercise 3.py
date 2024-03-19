# Write a program to accept a string from the user and display characters that are present at an even index number.

question = input ("Please give a word: ")

for i in range (0, len(question),2):
    print(question[i])