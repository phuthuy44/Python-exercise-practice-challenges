
m = int(input("Nhap m :"))
#Viết chương trình nhập vào hai số M,N. In ra tất cả các số nguyên tố, số đối xứng, số hoàn chỉnh, số chính phương trong khoảng[M,N](Nếu có)
n = int(input("Nhap n :"))

def check_prime_number(n) : 
    if n < 2 :
        return False
    for i in range(2,n):
        if n % i == 0 :
            return False
    return True

def symmetrical_num(n) :
    st = str(n)
    #l = len(st)
    #st1 =''
    if (st[::-1]==st) :
        return True
    return False 

def lietke_prime_number(m,n):
    print("Cac so nguyen to trong khoang [",m, ",",n,"]: ")
    for i in range(m,n+1):
        if check_prime_number(i):
            print(i, end=' ')
    return False

def lietke_symmertrical_number(m,n):
    print("\r")
    print("Cac so doi xung trong khoang [",m,",",n,"]: ")
    for i in range(m,n+1):
        if symmetrical_num(i):
            print(i, end=' ')
    return False

def check_so_hoan_hao(n):
    s = 0
    for i in range(1,n):
        if n % i == 0 :
            s += i 
    if s == n :
        return True
    return False 

def lietke_so_hoan_ha(m,n):
    print("\r")
    print("Cac so hoan hao trong khoang [",m,",",n,"]: ")
    for i in range(m,n+1):
        if check_so_hoan_hao(i):
            print(i,end = ' ')
    return False

def check_square_number(n):
    if any(i**2 == n for i in range(n+1)) :
        return True
    else :
        return False

def lietke_square_number(m,n):
    print("\r")
    print("Cac so hoan hao trong khoang [",m,",",n,"]: ")
    for i in range(m,n+1):
        if(check_square_number(i)) :
            print(i,end=' ')
    return False

lietke_prime_number(m,n)
lietke_symmertrical_number(m,n)
lietke_so_hoan_ha(m,n)
lietke_square_number(m,n)
