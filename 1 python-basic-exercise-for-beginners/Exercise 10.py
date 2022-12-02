# Create a new list from a two list using the following condition
# Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers
# from the first list and even numbers from the second list.

def frankenstein(list1,list2):
    new_list = []
    for i in list1:
        if i %2 !=0:
            new_list.append(i)
    for j in list2:
        if j %2 ==0:
            new_list.append(j)
    return new_list

print(frankenstein([10, 20, 25, 30, 35], [40, 45, 60, 75, 90]))
# result list: [25, 35, 40, 60, 90]