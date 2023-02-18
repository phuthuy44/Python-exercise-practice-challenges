#Print the sum of the current number and the previos number
n = int(input("Enter n:"))

def printTheSum(n):
    previous_num = 0
    for i in range(1,n):
        s = previous_num + i
        print("Current number", i,"Previous number",previous_num,"Sum = ", s)
        previous_num = i

printTheSum(n) 