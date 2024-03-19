# Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number
from typing import Tuple


# Given:
#
# sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
#
# Expected Outcome:
#
# unique items [87, 45, 41, 65, 99]
# tuple (87, 45, 41, 65, 99)
# min: 41
# max: 99

def removeDuplicates(numbers: list[int]) -> list[int]:
    new_numbers = []
    for number in numbers:
        if number not in new_numbers:
            new_numbers.append(number)
    return new_numbers


def createTuple(numbers: list[int]) -> tuple[int, ...]:
    return tuple(numbers)


def getMinMax(numbers: tuple[int, ...]) -> tuple[int, int]:
    return min(numbers), max(numbers)


def main():
    sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
    new_sample_list = removeDuplicates(sample_list)
    sample_list_tuple = createTuple(new_sample_list)
    minimum, maximum = getMinMax(sample_list_tuple)
    print(f"unique items: {new_sample_list}")
    print(f"tuple: {sample_list_tuple}")
    print(f"min: {minimum}\nmax: {maximum}")

main()
