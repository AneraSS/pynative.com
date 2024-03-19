# Write a program to display all prime numbers within a range

start = 25
end = 50

def is_prime(num):
    for i in range(2,num):
        if num %i == 0:
            return False
    return True

for number in range(start,end+1):
    if is_prime(number):
        print(number)
