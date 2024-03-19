# Check if the first and last number of a list is the same

def is_the_same(list):
    return list[0] == list[-1]


print(is_the_same([1, 2, 3, 6, 1]))
print(is_the_same([2,3,5,6,7]))
print(is_the_same([2,4,5,2]))

# ili:
# def is_the_same(list):
#     if list[0] == list[-1]:
#         return True
#     else:
#         return False