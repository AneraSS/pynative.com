# Exercise 9: Display numbers from -10 to -1 using for loop



def option_one(number):
    for i in reversed(range(1,number+1)):
        print(f"-{i}")


def option_two(number):
    for num in range(-number, 0, 1):
        print(num)

option_two(10)