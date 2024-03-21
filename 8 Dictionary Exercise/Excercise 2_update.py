# Exercise 2: Merge two Python dictionaries into one
#
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#
# Expected output:
#
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}


def mergeDict(dict1: dict, dict2:dict) -> dict:
    dict3 = dict1.copy()
    dict3.update(dict2)
    dict4 = {}
    dict4.update(dict1)
    dict4.update(dict2)
    return dict3


def mergeDict2(dict1: dict, dict2:dict) -> dict:
    dict3 = {}
    dict3.update(dict1)
    dict3.update(dict2)
    return dict3


def main():
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    print(f"Mege 2 to 1, option 1: {mergeDict(dict1, dict2)}")
    print(f"Mege 2 to 1, option 2: {mergeDict2(dict1, dict2)}")

main()