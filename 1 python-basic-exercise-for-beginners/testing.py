# https://pynative.com/python-basic-exercise-for-beginners/

# Excercise 1

def product_or_sum(num1, num2):
    solution = 0
    if (num1 * num2) <= 1000:
        solution = num1 * num2
    else:
        solution = num1 + num2
    return solution

# print (product_or_sum(40,30))

# Excercise 2
def print_sum (n):
    for i in range (0, n):
        current_num = i
        if i-1 >=0:
            previous_num = i-1
        else:
            previous_num = 0
        sum = current_num + previous_num

        print (f"Current Number {current_num} Previous Number  {previous_num}  Sum:  {sum}")


# print_sum(10)

# Excercise 3

def print_even(string):
    print (f"Original string is {string}.")
    print ("Printing only even index chars.")
    string = str(string)
    for letter in range(0,len(string),2):
        print(string[letter])

#print_even('pynative')

# Excercise 4

def remove_char (string,number):
    new_string = string[number:]
    return new_string

# print (remove_char('pynative',4))

# Excercise 5

def is_same(list_number):
    if list_number[0] == list_number[-1]:
        return True
    else:
        return False

#print(is_same([10, 20, 30, 40, 10]))
#print(is_same([75, 65, 35, 75, 30]))

#Excercise 6

def divisible_by5(list_numbers):
    print (f"Given list is: {list_numbers}")
    print ("Divisible by 5")
    for num in list_numbers:
        if num %5 == 0:
            print(num)

#divisible_by5([10, 20, 33, 46, 55])

# Excercise 7

def count_Emma(string):
    count = 0
    for i in range(0, len(string)):
        substring = string[i:i+4]
        if substring == 'Emma':
            count +=1
    return count

#print (count_Emma("Emma is good developer. Emma is a writer"))

#Excercise 8

def print_pattern(number):
    for i in range(1, number+1): # prints first number in row
        line = []
        for j in range (0, i): # prints all elements in same row
            line.append(i)
        print(line)


#print_pattern(5)

def print_pattern_string(number):
    for i in range (1,number+1): # prints first number in row
        line = ' '
        for j in range (0,i): # creates all the numbers per row
            string = str(i)
            line += string + ' ' # appending
        print(line)


#print_pattern_string(5)

# Excercise 9

# Excercise 10
def combine_lists(list1, list2):
    new_list = []
    for num in list1:
        if num %2 != 0:
            new_list.append(num)
    for num in list2:
        if num %2 == 0:
            new_list.append(num)
    return new_list

#print (combine_lists([10, 20, 25, 30, 35], [40, 45, 60, 75, 90]))

# Excercise 11
# Excercise 12

def calculate_tax(paycheck):
    if paycheck < 10_000:
        tax = 0
        return tax
    elif (paycheck > 10_000) and (paycheck < 20_000):
        tax = (paycheck-10000)*0.1
        return tax
    elif paycheck > 20_000:
        tax = (paycheck-20_000)*0.2 + 10000*0.1
        return tax

#print(calculate_tax(45_000))

# Excercise 13

def print_multiplication(number):
    for i in range (1,number+1):
        list = []
        for j in range (1,number+1):
            multiply = i*j
            list.append(multiply)
        print(list)

#print(print_multiplication(10))

def print_multiplication_string(number):
    for i in range (1,number+1):
        list = ''
        for j in range (1,number+1):
            multiply = i*j
            list += str(multiply) + ' '
        print(list)

#print(print_multiplication_string(10))

def downward_halfpyramid(number):
    for i in reversed(range (1,number+1)):
        asterisk = '* '
        for j in range (1, number+1):
            same_row = asterisk * i
        print(same_row)

#downward_halfpyramid(5)

#Excercise 15

def exponent_base(base, exponent):
    result = 1
    for i in range(1, exponent+1):
        result = result*base
    print(result)

#exponent_base (2,5)

# Excercise 14