# Exercise 5: Count all letters, digits, and special symbols from a given string

def count(string):
    counter =  0
    for char in string:
        counter +=1
    print(f"All characters = {counter}")

count('P@#yn26at^&i5ve')

def count_all(string):
    alpha_counter = 0
    digit_counter = 0
    symbol_counter = 0

    for char in string:
        if char.isalpha():
            alpha_counter +=1
        elif char.isdigit():
            digit_counter += 1
        else:
            symbol_counter +=1
    print (f"Charts = {alpha_counter} \nDigits = {digit_counter} \nSymbols = {symbol_counter} ")

count_all('P@#yn26at^&i5ve')
