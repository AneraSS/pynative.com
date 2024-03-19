
original = 'PyNaTive'
print(f"Original string is: {original}")
lower = ''
upper = ''

for char in original:
    if char.islower():
        lower += char
    else:
        upper += char

print(f"Resulting string: {lower+upper}")
# result: yaivePNT
