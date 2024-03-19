# Write a program to find how many times substring “Emma” appears in the given string.

def find_substring(string_name):
    counter = 0
    for i in range(0, len(string_name)):
        substring = string_name[i: i + 4]
        if substring == 'Emma':
            counter +=1
    return counter

print (find_substring("Emma is good developer. Emma is a writer"))