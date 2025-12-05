# import pyjokes
# print(pyjokes.get_joke())
# import pyjokes
# print(pyjokes.get_joke())

# import pyttsx3
# engine=pyttsx3.init()
# volume = engine.getProperty('volume')
# engine.setProperty('volume', 100) 
# engine.say("my number is \"9 1 0 3 0 4 2 2 3 1\"")
# engine.runAndWait()

# import pyttsx3
# engine = pyttsx3.init()
# volume =engine.getProperty('volume')
# engine.setProperty('volume' ,100)
# engine.say("hey jamid")
# engine.runAndWait()
# import pyttsx3
# engine = pyttsx3.init()
# volume = engine.getProperty('volume')
# engine.setProperty('volume',0.99)
# engine.say("hi jamid")
# engine.runAndWait()
# Python program to
# demonstrate pyperclip module


# This will import pyperclip
# import pyperclip
# pyperclip.copy("Hello world !")
# pyperclip.paste()

# pyperclip.copy("Isn't pyperclip interesting?")
# pyperclip.paste()

# a= int(input("enter the value of a"))
# sq=a**2
# print(sq)

# name  = "harry is a tacher"
# length = len(name)                                   FOR LENGTH
# print(length)

# nameshort = name[]                                   FOR SLICE
# slice = name[0:10]                                   ending endex is not included it will only print 0 to 9
# print(slice)

# character3 = name[3]                                 FOR 1 CHARRACTER
# print(character3) 


# print(name[-2:-1])                                      negative index


# print(name[:3])                                           it will print 0 to 2 charracters [0:3]
# print(name[1:])                                           it will print the length of the string from index 1


# slice with skip value

# word = "amazing".                       
# skip = word[1:4:2]
# print(skip)


# name = "jamidfayaz"
# skip = name[2:9:3]
# print(skip)
# a=10
# b=20
# c=6
# d=b%c+a*b
# print(d)
# n = int (input("enter the value of n"))

# for i in range (1,n+1) :
#     if (i==1 or i==n):
#         print("*"*n,end="")
#     else:
#         print("*",end="")
#         print(" "*(n-2), end="")
#         print("*",end="")

#         print()
# for i in range(1,n+1):
#     print("*"*i,end="")
#     print(" "*(n-i),end="")
#     print()

# 
# def greeting(name):
#     print(f"hello, {name} welcome to python world")
# greeting("aqib")
# 
# def calculate_bill(meal_cost, tax_rate, tip_percentage):
#     tax_amount = meal_cost * tax_rate
#     tip_amount = meal_cost * tip_percentage
#     total_amount = tip_amount + tax_amount + meal_cost
#     return total_amount
# bill_amount=calculate_bill(7898,0.9,0.2)
# print(f"the total bill is:,{bill_amount}")


# def convertor(ferinite):
#     cel=(ferinite - 32) * 5/9
#     return cel

# con= convertor(32)
# print(f"the converted value is,{con}")

# def is_in_range(number,min_value,max_value):
#     if min_value<=number<=max_value:
#         return True
#     else:
#         return False
    
# check=is_in_range(234,-1111,1111)
# print(f"is the number in the range: {check}")
# def factorial(n):
#     if n==1 or n==0:
#         return 1
#     return n*factorial(n-1)
# n = int(input("enter your number"))
# print(f"the factorial of {n} is : {factorial(n)}")
# def greatest(num1,num2,num3):
#     if num1>num2 and num1>num3:
#         return num1
#     elif num2>num1 and num2>num3:
#         return num2
#     else:
#         return num3
# num1 = int(input("enter your number"))
# num2 = int(input("enter your number"))
# num3 = int(input("enter your number"))
# print(f"greatest number is: {greatest(num1,num2,num3)}")
def sum_of_n(n):
    
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
n = int(input("enter your number"))
print(f"sum={sum_of_n(n)}")
    
    





