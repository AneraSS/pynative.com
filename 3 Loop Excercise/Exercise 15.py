# Exercise 15: Use a loop to display elements from a given list present at odd index positions

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
new_list = []

for number in my_list[1::2]:
    new_list.append(number)

print(new_list)