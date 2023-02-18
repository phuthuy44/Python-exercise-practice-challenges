#Return multipe values from a function

def calculateion():
    a = int(input("Enter a :"))
    b = int(input("Enter b:"))
    add = a+b
    subtraction = a - b
    return add, subtraction

res = calculateion()
print(res)