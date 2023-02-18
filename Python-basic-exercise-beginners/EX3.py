# Print characters from a string that are present at an even index number
def even_index():
    word = input("Enter a string: ")
    Strings = len(word)
    #iteracte a each character of a string
    #start: 0 to start with first character
    #stop : Strings-1 because index starts with 0 
    #step : 2 to get the characters present at even index like 0,2,4
    for i in range(0,Strings-1,2):
        print(word[i])

even_index()