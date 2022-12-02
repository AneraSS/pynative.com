# Exercise 18: Print the following pattern
# Write a program to print the following start pattern using the for loop

n = 5
asterisk = '* '
row = ''
for i in range (1,n+1):
    for j in range (1, i+1):
        row = asterisk*j
    print (row)
for i in reversed(range(1,n)):
    for j in range (1, i+1):
        row = asterisk*j
    print (row)