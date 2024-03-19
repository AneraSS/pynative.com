# Exercise 1: Reverse a list in Python
#
# Given:
#
# list1 = [100, 200, 300, 400, 500]
#
# Expected output:
#
# [500, 400, 300, 200, 100]

# .reverse() returns None, therefore you need to make a copy
def reverseList(numbers: list[int]) -> list[int]:
    new_numbers = numbers.copy()
    new_numbers.reverse()
    return new_numbers

def foo():
    return None

def bar():
    return foo()

print(bar())

def main():
    list1 = [100, 200, 300, 400, 500]
    new_list = reverseList(list1)
    print(new_list)

main()

#