# Exercise 2: Concatenate two lists index-wise
#
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item
# from both the list, then the 1st index item, and so on till the last element. any leftover items
# will get added at the end of the new list.

# Given:
#
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
#
# Expected output:
#
# ['My', 'name', 'is', 'Kelly']


# zips same length, leftovers are not added!
# Code given as a solution for this exercise!
def ConcatenateTwoLists_solution(list1: list[str], list2: list[str]) -> list [str]:
    list3 = [i + j for i, j in zip(list1, list2)]
    return list3


# lists have to be of same length, otherwise: Error!
def ConcatenateTwoLists_alt(list1: list[str], list2: list[str]) -> list [str]:
    list3 = []
    for index in range(len(list1)):
        list3.append(list1[index]+list2[index])
    return list3


# any leftover is added at the end of the list!
def ConcatenateTwoLists_ChatGPT(list1: list[str], list2: list[str]) -> list [str]:
    result = []
    for i in range(max(len(list1), len(list2))):
        if i < len(list1) and i < len(list2):
            result.append(list1[i] + list2[i])
        elif i < len(list1):
            result.append(list1[i])
        elif i < len(list2):
            result.append(list2[i])
    return result


def main():
    list1 = ["M", "na", "i", "Ke"]
    list2 = ["y", "me", "s", "lly", "Rowland", "Junior"]
    print(f"Solution by the book: {ConcatenateTwoLists_solution(list1, list2)}")
    #print(f"Alternative solution, as per book solution: ConcatenateTwoLists_alt(list1, list2)")
    print(f"Solution by ChatGPT: {ConcatenateTwoLists_ChatGPT(list1, list2)}")

main()

# BOOK: doesn't work as it should!
# ALT: doesn't work as it should!

# ChatGPTs alternatives to zip:
# ALTERNATIVE 1
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# list3 = list(map(lambda x, y: x + y, list1, list2))
# print(list3)

# ALTERNATIVE 2
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# list3 = []
#
# for i in range(min(len(list1), len(list2))):
#     list3.append(list1[i] + list2[i])
#
# print(list3)
