#Liệt kê tất cả các số nguyên tố nhỏ hơn N(N nhập từ bàn phím)
n = int(input("Enter n:"))

def check_prime_number(n):
    if n < 2 :
        return False
    for i in range(2,n):
        if n % i == 0 :
            return False
    return True

def lietke_nhohon_n(n):
    print("Liet ke cac so nguyen to nho hon",n,"la: ")
    for i in range(2,n+1):
        if check_prime_number(i):
            print(i,end=' ')
        
lietke_nhohon_n(n)