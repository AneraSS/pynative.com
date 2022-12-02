# Exercise 13: Print multiplication table form 1 to 10


def multiplication_table():
    """Create row index"""
    for row_index in range (1,11):
        print(convert(make_row(row_index)))


def make_row(row_idx):
    """Multiply that line"""
    redak = []
    for number in range (1,11):
        var1 = row_idx * number
        redak.append(var1)
    return redak


def convert (numbers):
    """Turns integer into string."""
    string_list = ''
    for number in numbers:
         string_list = string_list + ' ' + (str(number))
    return string_list


multiplication_table()



