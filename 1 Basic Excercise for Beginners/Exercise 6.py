# Iterate the given list of numbers and print only those numbers which are divisible by 5


def divisible_by5 (numbers):
    new_list = []
    for number in numbers:
        if number %5==0:
            new_list.append(number)
    return new_list


print(divisible_by5([1,2,3,5,10,25,35]))
print(divisible_by5([0,-5,3]))