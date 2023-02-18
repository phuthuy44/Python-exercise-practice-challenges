#Append new string in the middle of a given string

def append_string():
    s1 = input("Enter a s1 :")
    s2 = input("Enter a s2:")

    middle = int(len(s1)/2)
    x = s1[:middle:] # get character from 0 to the middle index number form s1

    x += s2
    x += s1[middle:]
    print(x)
append_string()