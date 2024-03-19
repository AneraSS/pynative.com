# Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a
# dictionary. If not, delete it from the list.

# Given:
#
# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'John':47, 'Emma':69, 'Kelly':76, 'Jason':97}
#
# Expected Outcome:
#
# After removing unwanted elements from list [47, 69, 76, 97]


def removeKeys(numbers: list[int], name_to_age: dict[[str], [int]]) -> list[int]:
    for number in numbers.copy():   # because a change is made in-place and iteration is made at same time
        if number not in name_to_age.values():
            numbers.remove(number)
    return numbers


def main():
    roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
    sample_dict = {'John': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}
    result = removeKeys(roll_number, sample_dict)
    print(result)

main()

# zasto vrati 95 isto?