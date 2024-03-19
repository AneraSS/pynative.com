# Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates

# Given:
#
# speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
#
# Expected Outcome:
#
# [47, 52, 44, 53, 54]


def getValues(month_to_number: dict[[str], [int]]) -> list[int]:
    values = []
    for v in month_to_number.values():
        if v not in values:
            values.append(v)
    return values

def main():
    speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
    result = getValues(speed)
    print(result)

main()