# Print the following pattern
# Write a program to use for loop to print the following reverse number pattern

number = 5

def opcija1(number):
    for i in reversed(range (1, number+1)): # 1st in row; reversed up-down
        row = ''
        for j in reversed(range (1, i+1)): # reversed within a row
            row = row + ' ' + str(j)
        print (row)

def opcija2(number):
    for i in range (number, 0, -1): # 1st in row; reversed up-down
        row = ''
        for j in range (i, 0, -1): # reversed within a row
            row = row + ' ' + str(j)
        print(row)

#opcija2(number)

def anerin_range(start,stop,step=1):
    list = []
    if step > 0:
        while start < stop:
            list.append(start)
            start = start + step
        return list
    elif step < 0:
        while start > stop:
            list.append(start)
            start = start + step
        return list
    else:
        raise Exception("Step cannot be 0.")

def anerin_range2(start,stop,step=1):
    if step == 0:
        raise Exception("Step cannot be 0.")

    list = []
    while ((step > 0) and (start < stop)) or ((step < 0) and (start > stop)):
        list.append(start)
        start = start + step
    return list




print(anerin_range2(30,10,-1))