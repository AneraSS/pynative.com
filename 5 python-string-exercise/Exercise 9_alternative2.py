# Exercise 9: Calculate the sum and average of the digits present in a string
#
# Given a string s1, write a program to return the sum and average of the digits that appear in the string,
# ignoring all other characters.

str1 = "PYnative29@#8496"
#Sum is: 38 Average is  6.333333333333333

# from a string of mixed char extracts digits into a list of integers
def extractDigits(str):
    digits = []
    for char in str:
        if char.isdigit():
            digits.append(int(char))
    return digits

# from a list of number calculates sum and average
# average = sum / numbers
def calculateSumAverage(digits):
    average = sum(digits) / len(digits)
    return f"Sum is: {sum(digits)}, average is: {average}"


print(calculateSumAverage(extractDigits(str1)))