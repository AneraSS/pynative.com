# Exercise 2: Print the following pattern
# Write a program to print the following number pattern using a loop.

for i in range (1,6): # first number per row
    line = ''
    for j in range (1,i+1): # iteration within row
        line = line + str(j) + ' ' # collecting values
    print(line)
