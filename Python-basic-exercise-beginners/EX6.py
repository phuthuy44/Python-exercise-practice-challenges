#Create an inner function to calculate the addition in the following way

def outer_fun(a,b):
    
    def add(a,b):
        return a+b
    addition = add(a,b)
    return addition + 5

res = outer_fun(10,20)
print(res)