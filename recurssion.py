# def factorial(n):
#     if n==1 or n==1:
#         return 1
#     return n*factorial(n-1) #function calls itself again and again
# 
# print(f"the facorial of the nomber {n} is : {factorial(n)}")

# def gratest():
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# a = int (input("enter the the number 2: "))
# b = int (input("enter the the number 2: "))
# c= int (input("enter the the number 3: "))
# print(f"the greater number is  : {gratest()}")

# def sum(n):
#     if n == 0:
#         return 0
#     # else:
#     #     return 0
#     return  n + sum(n-1)
# n = int (input("enter the the number 2: "))
# print(f"the sum is : {sum(n)}")
    
def fib(n):
    if n<=1:
        return 1
    return fib(n-1)+fib(n-2)
n=int(input("enter the value of n"))
for i in range(n):
    print(fib(i)," ",end=" ")





#decimal to binary
def dec_to_bin(n):
    if n < 2:              # base case
        return str(n)
    return dec_to_bin(n // 2) + str(n % 2)   # recursive call

n = int(input("Enter a decimal number: "))
print("Binary:", dec_to_bin(n))


#dec to hexa
hex_digits = "0123456789ABCDEF"

def dec_to_hex(n):
    if n < 16:               # base case
        return hex_digits[n]
    return dec_to_hex(n // 16) + hex_digits[n % 16]   # recursive call

n = int(input("Enter a decimal number: "))
print("Hexadecimal:", dec_to_hex(n))
