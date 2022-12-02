# Exercise 5: Display numbers from a list using loop
# Write a program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]


def option1(numbers):
    for number in numbers:
        if number % 5 == 0:
            if number <= 150:
                print(number)
            elif number > 500:
                break


def option2(numbers):
    for number in numbers:
        if number > 500:
            break
        if number > 150:
            continue
        if number % 5 == 0:
            print(number)


option2(numbers)
