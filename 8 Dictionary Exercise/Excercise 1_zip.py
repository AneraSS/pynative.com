# Exercise 1: Convert two lists into a dictionary
#
# Below are the two lists. Write a Python program to convert them into a dictionary in a way that
# item from list1 is the key and item from list2 is the value
#
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# Expected output:
#
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}


def listToDict(list1:list[str], list2:[int]) -> dict:
    list1_to_list2 = {}

    for index in range(len(list1)):
        # list1_to_list2.update({list1[index]:list2[index]})
        list1_to_list2[list1[index]] = list2[index] #dict[key] = value

    return list1_to_list2

print(dict([(1,2), (3,4)]))

def listToDict_zip(list1: list[str], list2: [int]) -> dict:
    list1_to_list2 = dict(zip(list1, list2))
    return list1_to_list2


def main():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    print(f"Lists to Dictionary, option 1: {listToDict(keys, values)}")
    print(f"Lists to Dictionary, option 2: {listToDict_zip(keys, values)}")


main()