#In ra màn hình M số nguyên tố đầu tiên 
m = int(input("Enter m :"))

def check_prime_number(m):
    """
    It returns True if the number is prime, and False if it is not
    
    :param m: the number to be checked
    :return: True or False
    """
    if m < 2:
        return False
    for i in range(2,m):
        if m%i ==0 :
            return False
    return True

def lietke_M_songuyento_dautien(m):
    """
    It prints the first m prime numbers
    
    :param m: the number of prime numbers to be displayed
    """
    print("Liet ke",m,"so nguyen to dau tien la: ")
    count = 0
    i = 2
    sb =[]
    while(count < m):
        if check_prime_number(i):
           # Adding the value of i to the list sb.
            sb.append(str(i))
            count += 1
        i += 1 
    print(" ".join(sb))
        

lietke_M_songuyento_dautien(m)