def addition(num1,num2):
    return num1+num2

def substraction(num1,num2):
    return num1-num2

def multiplication(num1,num2):
    return num1*num2

def division(num1,num2):
    try:
        return num1/num2
    except:
        ZeroDivisionError
    return "Cannot be divided by zero."




num1=float(input("Enter first number=="))
num2=float(input("Enter second number=="))

print(addition(num1,num2))
print(substraction(num1,num2))
print(multiplication(num1,num2))
print(division(num1,num2))