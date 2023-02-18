#Calculate the multiplication and sum of two numbers
number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))

def multiplication_sum(number1,number2):
    multipplication = number1*number2

    if multipplication <= 1000 :
        return multipplication
    else :
        return number1 + number2

print("The result is :",multiplication_sum(number1,number2))