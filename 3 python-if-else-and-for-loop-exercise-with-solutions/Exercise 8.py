# Exercise 8: Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]

def option_one(list1):
    for i in range(1, len(list1)+1):
        position = -i
        print (list1[position])

def option_two(list1):
    list2 = reversed(list1)
    for number in list2:
        print(number)

#option_one(list1)
option_two(list1)