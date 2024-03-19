# Exercise 9: Find the largest item from a given list
# x = [4, 6, 8, 24, 12, 2]

list = [4, 6, 8, 24, 12, 2]
biggest = []


for i in range(0,len(list)):
    if list[i] > list[i-1]:
        biggest = list[i]

print(biggest)

# ili
print(max(list))

