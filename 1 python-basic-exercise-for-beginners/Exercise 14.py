# Print downward Half-Pyramid Pattern with Star (asterisk)


def make_new_row(n):
    for i in range (0,n+1):
        print(make_asterisk(i))

def make_asterisk(n):
    one_row = 0
    for i in range (1,n+1):
        asterisk = '* '
        one_row = asterisk * (n+1-i)
        return one_row

make_new_row(5)