# Create a new string made of the first, middle, and last characters of each input string
# Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

# result AJrpan

s1 = 'America'
s2 = 'Japan'

def mix_str(s1,s2):
    #from 1st string
    first1 = s1[0]
    middle1 = s1[int(len(s1)/2)]
    last1 = s1[-1]
    #from 2nd string
    first2 = s2[0]
    middle2 = s2[int(len(s2)/2)]
    last2 = s2[-1]
    print(first1+first2+middle1+middle2+last1+last2)

mix_str('America','Japan')