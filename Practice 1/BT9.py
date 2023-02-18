#Viet chuong trinh tinh luy thua nanh dung de quy va chia de tri
import sys
a = int(input("Enter a:"))
b = int(input("Enter b:"))
'''def power(a,b):
    if a==0 :
        return 0
    elif b==0:
        return 1
    elif b==1:
        return a
    else:
        return a*power(a,b-1)
    
print(a,"^",b,"=",power(a,b))
'''
sys.setrecursionlimit(10**6)
def fastpower_divideandconquer(a,b):
    if b == 1 :
        return a
    else :
        x = fastpower_divideandconquer(a,b/2)
        if b % 2 == 0:
            return x*x
        else :
            return x*x*a


print(a,"^",b,"=",fastpower_divideandconquer(a,b))