#for loop   and while loop
# for i in range(1,6):
#     print(i)
# else:
#     print("done")
  #while loop
# i = 0
# while(i<6):
#     print(i)
#     i = 1+i


# list =[ 12, "jamid", 123, "aqib", "majid", 1234]
# i = 0
# while(i<len(list)):
#     print(list[i])
#     i = 1+i

#for loop with else
# for i in range(1,6):
#     print(i)
# else:
#     print("done")


#factorial for loop

# 

# product = 1
# for i in range (1,n+1):
#     product = product*i
# print(f"the factorial of a {n} is {product}")




#while loop



# i=1

# product = 1
# while(i<=n):
#     product=product*i
#     i = i+1
# print(f"the factorial of {n} is {product}")



#star pattern
# n = int (input("entr the number"))

# for i in range (1,n+1):
#     print(" "*(n-i), end="")
#     print("*" * (2*i-1), end="")
#     print()
    
# n = int (input("enter the number"))

# for i in range (1,n+1):
#     # print(" "*(n-i), end="")
#     print("*" * i , end="")
#     print()
# n = int (input("enter the number"))
# for i in range (1, n+1):
#     if (i==1) or (i==n):
#         print("*"*n)
#     else:
#         print("*", end="")
#         print(" " * (n-2) , end="")
#         print("*",end="")
#         print("")
#       if (n-i==0):
#         print("*" * n, end="" )
# else:
#         print("*")
#         print(" ")
#         print("*")
#decimal to binary!
n = int(input("enter a decimal number: "))

binary = ""

while n > 0:
    r = n % 2         # take remainder
    binary = str(r) + binary   # store in reverse
    n = n // 2        # update n

print("Binary:", binary)





# decimal to hexadecimal

    
    

n = int(input("Enter decimal number: "))

hex_digits = "0123456789ABCDEF"
hexadecimal = ""

while n > 0:
    remainder = n % 16
    hexadecimal = hex_digits[remainder] + hexadecimal
    n = n // 16

print("Hexadecimal:", hexadecimal)
