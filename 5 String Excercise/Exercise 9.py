# Exercise 9: Calculate the sum and average of the digits present in a string
#
# Given a string s1, write a program to return the sum and average of the digits that appear in the string,
# ignoring all other characters.

str1 = "PYnative29@#8496"
#Sum is: 38 Average is  6.333333333333333

# from a string of mixed characters extracts numbers and calculates sum (int)
def extractSum(str):
    sum = 0
    for char in str:
        if char.isdigit():
            sum += int(char)
    return sum

# from a string of mixed characters extracts numbers and calculates average (int)
# average = sum / numbers
def getAverage(str):
    sum = extractSum(str)
    count = 0
    for char in str:
        if char.isdigit():
            count += 1
    average = sum / count
    return average


print(f"Sum is: {extractSum(str1)}")
print(f"Average is: {getAverage(str1)}")