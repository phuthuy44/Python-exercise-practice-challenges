#Viết chương trình nhập vào một số nguyên n. Kiểm tra xem số đó có phải là số nguyên tố, số đối xứng, số hoàn chỉnh, số chính phương hay không?

def symmetrical_num(n) :
    st = str(n)
    #l = len(st)
    #st1 =''
  
    if (st[::-1]==st) :
        return 1
    return 0

def check_prime_number(n) : 
    if n < 2 :
        return 0
    for i in range(2,n):
        if n % i == 0 :
            return 0
    return 1

def check_so_hoan_hao(n):
    s = 0
    for i in range(1,n):
        if n % i == 0 :
            s += i 
    if s == n :
        return 1
    return 0

def check_square_number(n):
    if any(i**2 == n for i in range(n+1)) :
        return 1
    return 0

'''symmetrical_num(n)
check_prime_number(n)
check_so_hoan_hao(n)
check_square_number(n)'''

def check():
    while True :
        try :
            n = int(input("Enter n :"))
            if n < 0:
                print("Invalid input")
                continue
            break
        except ValueError :
            print("Invalid input")
            #check()
    flag_prime = False
    flag_so_hao = False
    flag_square = False
    flag_symmetrical = False

    if symmetrical_num(n) :
        flag_symmetrical = True
        print(n,"is symmetrical")
    if check_prime_number(n) :
        flag_prime = True
        print(n,"is prime number")
    if check_so_hoan_hao(n) :
        flag_so_hao = True
        print(n,"is perfect number")
    if check_square_number(n) :
        flag_square = True
        print(n,"is square number")

check()




