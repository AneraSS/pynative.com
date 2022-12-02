# Exercise 5: Accept a list of 5 float numbers as an input from the user

# float numbers: it is a number that has a decimal place

def option1():
    list_numbers = []
    for i in range (1,3):
        number = input(f"Please, enter {i}. number: ")
        number = float(number)
        list_numbers.append(number)
    print(list_numbers)

#option1()

# split() - by default is whitespace

def option2():
    raw_numbers = input("Please give 5 float numbers separated by space: ")
    number_list = raw_numbers.split()
    new_list = []
    for number in number_list:
        floated = float(number)
        new_list.append(floated)
    print (new_list)

#option2()


def my_split_method(your_string, separator=" "):
    #your_string += separator # zato jer na zadnjem nema razmaka pa nikad nece biti dodan u listu osim s dolje if-om
    string_list = []
    new_string = ""
    for char in your_string:
        # new_string += char
        if char != separator:
            new_string += char
        else:
            #new_string = new_string.strip() # strip sam po sebi nije trajan, eq. sort/sorted
            if new_string != "":
                string_list.append(new_string)
            new_string = ""
    if new_string != "": # ovo je za ovaj zadnji koji ostaje lebdjeti umjesto da je dodan jer nakon zadnjeg nema space, alternativno moja prva linija
        string_list.append(new_string)
    return string_list

print(my_split_method("Anera Martin "))

