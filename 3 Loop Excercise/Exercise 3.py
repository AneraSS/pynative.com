# Calculate the sum of all numbers from 1 to a given number
# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
#
# For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

number = input("Enter number: ")
number = int(number)
sum = 0
for i in range (1, number+1):
    sum = sum + i
print(sum)