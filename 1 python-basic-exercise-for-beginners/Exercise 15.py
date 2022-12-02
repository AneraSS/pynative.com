# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.

def base_exponent(base, exponent):
    solution = base ** exponent

    solution2 = 1
    for i in range (1, exponent+1):
        solution2 = solution2 * base

    counter = 1
    solution3 = 1
    while counter <= exponent:
        counter +=1
        solution3 *= base

    print (f"{base} raises to the power of {exponent}: {solution}, or {solution2} or {solution3}")



base_exponent(2,5)