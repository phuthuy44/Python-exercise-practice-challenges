#Create a string made of the first, middle, and last character.

def create_string():
    string = input("Enter a string:")
    res = string[0] #get first character
    l = len(string) #get string size 
    mi = int(l/2) # get middle index number
    res += string[mi]  #get middle character and add it to result
    res = res + string[l-1]
    print(res)

create_string()