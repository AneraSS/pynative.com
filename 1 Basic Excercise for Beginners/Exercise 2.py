# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

for i in range (0,10):
    current_number = i
    previous_number = i-1
    if previous_number < 0:
        previous_number = 0
    sum = current_number + previous_number
    print(f" Current number {current_number}, previous number {previous_number}, sum: {sum}")