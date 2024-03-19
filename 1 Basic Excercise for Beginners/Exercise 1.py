# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

number1 = 40
number2 = 30

product = number1 * number2
sum = number1 + number2

if product <= 1000:
    print (product)
else:
    print (sum)
