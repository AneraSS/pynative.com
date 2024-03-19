# Exercise 14: Remove empty strings from a list of strings

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# After removing empty strings
# ['Emma', 'Jon', 'Kelly', 'Eric']


new_list = []
for item in str_list:
    if item != "" and item != None:
        new_list.append(item)

print(new_list)


new_list = []
for item in str_list:
    if item:
        new_list.append(item)

print(new_list)