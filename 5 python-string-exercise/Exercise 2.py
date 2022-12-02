# Exercise 2: Append new string in the middle of a given string

def append_middle(first,second):
    dividing = int(len(first)/2)
    first_part= first[:dividing]
    second_part= first[dividing:]
    new_string = first_part+second+second_part
    print(new_string)

append_middle('Ault','Kelly')
# result: AuKellylt







