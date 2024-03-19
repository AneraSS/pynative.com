# Exercise 3: Turn every item of a list into its square
#
# Given a list of numbers. write a program to turn every item of a list into its square.
#
# Given:
#
# numbers = [1, 2, 3, 4, 5, 6, 7]
#
# Expected output:
#
# [1, 4, 9, 16, 25, 36, 49]

def getSquare(numbers:list[int]) -> list[int]:
    squares = []
    for number in numbers:
        squares.append(number*number)
    return squares

# using list comprehension:
# squares = [x * x for x in numbers]


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    print(getSquare(numbers))

main()