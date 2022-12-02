# Find the factorial of a given number
# Write a program to use the loop to find the factorial of a given number.
#
# The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.

number = 5
result = 1

for i in range(1,number+1):
    result = i * result
print(result)

def factoriel(x):
    if x == 1:
        return 1
    return x * factoriel(x-1)