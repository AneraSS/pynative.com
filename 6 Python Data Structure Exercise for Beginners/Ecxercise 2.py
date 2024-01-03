# Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second

# Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from
# the list l1 and even index elements from the list l2.

list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]

# Output:
#Element at odd-index positions from list one
#[6, 12, 18]
#Element at even-index positions from list two
#[4, 12, 20, 28]

#Printing Final third list
#[6, 12, 18, 4, 12, 20, 28]

for index in range (1, len(list1), 2):
    if index/2 == 0