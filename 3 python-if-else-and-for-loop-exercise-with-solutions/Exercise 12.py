# Display Fibonacci series up to 10 terms
# The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it.
# The first two numbers are 0 and 1.
# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34.
num1 = 0
num2 = 1
list = '0 1'

for i in range (1,9):
    sum = num1 + num2
    list = list + ' '+ str(sum)
    num1 = num2
    num2 = sum
print(list)
