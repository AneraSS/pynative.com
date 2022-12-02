# Exercise 8: Generate a Python list of all the even numbers between 4 to 30
# Expected Output: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

start = 4
end = 30
list = []

for i in range(start,end):
    if i%2 == 0:
        list.append(i)
print(list)

#or
print(list(range(4, 30, 2)))



