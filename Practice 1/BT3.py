#Tìm ước số chung lớn nhất và bội số chung nhỏ nhất của hai số a và b
a =int(input("Enter a:"))
b = int(input("Enter b:"))

def UCLN(a,b):
    """
    While a and b are not equal, subtract the smaller of the two from the larger, and return the smaller
    of the two when they are equal.
    
    :param a: the first number
    :param b: the number of bits in the key
    :return: The greatest common divisor of a and b.
    """
    while a != b :
        if a > b :
            a -= b 
        else :
            b -= a
    return a

def BCNN(a,b):
    result = UCLN(a,b)
    return int(a*b/result)

print("===========Khong dung de quy=======================")
print("Ước số chung lớn nhất của", a, "và", b, "là:", UCLN(a, b));
print("Bội số chung nhỏ nhất của", a, "và", b, "là:", BCNN(a, b));

def USCLN(a,b):
    """
    It returns the greatest common divisor of two numbers
    
    :param a: the first number
    :param b: the number of the first number
    :return: The greatest common divisor of a and b.
    """
    if(b==0):
        return a
    return USCLN(b,a % b)

def BSCNN(a,b):
    return int(a*b)/USCLN(a,b)

print("===========Dung de quy=======================")
print("Ước số chung lớn nhất của", a, "và", b, "là:", USCLN(a, b));
print("Bội số chung nhỏ nhất của", a, "và", b, "là:", BSCNN(a, b));
