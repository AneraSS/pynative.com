
num = 76542
reverse_number = 0
print("Given Number ", num)

while num > 0:
    last_digit = num % 10
    reverse_number = (reverse_number * 10) + last_digit
    num = num // 10
print("Revere Number ", reverse_number)
