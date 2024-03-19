# Exercise 6: Remove empty strings from the list of strings
#
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
#
# Expected output:
#
# ["Mike", "Emma", "Kelly", "Brad"]

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

for item in list1:
    if len(item) == 0:
        list1.remove(item)

print(list1)

# remove None from list1 and convert result into list
res = list(filter(None, list1))