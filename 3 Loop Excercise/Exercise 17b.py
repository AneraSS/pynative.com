# Exercise 17: Find the sum of the series upto n terms
# Write a program to calculate the sum of series up to n term.
# For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

def series_sum(digit, repeat):
    new_list = []
    for i in range(1,repeat+1): # broj iteracije
        new_list.append(gradi_broj(digit,i))
    print(new_list, sum(new_list))

    string_list = ''
    for number in new_list:
        string_list += str(number) + '+'
    print(string_list[:-1])


def gradi_broj(digit, broj_ponavljanja):
    number = 0
    for j in range(0, broj_ponavljanja):
        number = number * 10 + digit
    return number



series_sum(2,5)

# 0*10+2==2
# 2*10+2==22
# 22*10+2==222


