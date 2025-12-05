# num=(input("enter four digit number"))
# if len(num) != 4:
#     print ("invalid input")
# else:
#     d1=int(num[0])
#     d2=int(num[1])
#     d3=int(num[2])
#     d4=int(num[3])
# sumfirsttwo=d1+d2
# sumlasttwo=d3+d4
# if sumfirsttwo==sumlasttwo:
#     print("lucky number")
# else:
#     print("not a lucky number")

    
# num=int(input("enter number"))
# if num%3==0 and num%5==0:
#     print("fizzbuzz")
# elif num%3==0 and num%5!=0:
#     print("fizz")
# else:
#     print("buzz")
# num=int(input("enter number"))
# if -999<=num<=999:
#     print("yes it is a 3 digit number")
# else:
#     print("no. is not 3 digit number")
# num=int(input("enter number"))
# product=num*5
# if product%2==0:
#     print("even product")
# else:
#     print("odd product")
# angleone = int(input("enter angle one"))
# angletwo = int(input("enter angle two"))
# anglethree = int (input("enter angle three"))
# sum = angleone + angletwo+ anglethree
# if sum != 180:
#     print ("not a traingle")
# elif angleone and angletwo and anglethree <90:
#     print("acute traingle")
# elif angleone or angletwo or anglethree == 90:
#     print("right angled traingle")
# elif angleone or angletwo or anglethree >90:
#     print("obtuse traingle")

# char = input("Enter a character or symbol: ")
# asciivalue= ord(char)
# print(f"the ascii value of {char} is", asciivalue)
# 
# def palindrome():
#     string=(input("enter the string "))
#     if string==string[::-1]:
#         print("palindrome")
#     else:
#         print("not")


        
# palindrome()
    # for i in range(0,len(string)):
# def reverse_number(num):
#     rev = 0
#     for _ in range(len(str(num))):
#         digit = num % 10
#         rev = rev * 10 + digit
#         num = num // 10
#     return rev

# n = int(input("Enter a number: "))
# print("Reversed number:", reverse_number(n))



# # def reverse(s)
# def reverese_s():
#     rev=" "
#     for c in s:
#         rev=c+rev
#     return rev
# s=input("enter the string")
# print(reverese_s())

# #palindrome or not
# def palindrome():

#     if s==s[::-1]:
#         print("palindrome")
#     else:
#         print("not palindrome")
# s=input("enter a string")
# palindrome()

# def is_palindrome():
#     return s == s[::-1]
# s=input("enter a string")
# print(is_palindrome())

#febonacci series
# def f_s():
#     a, b = 0, 1
#     for i in range(0,10):
#         print(a, end=" ")
#         a,b = b,a+b
        
# f_s()

# #factorial
# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n - 1)

# print(fact(5))


# #largest element in lst
# l=[1, 2, 3, 4, 5, 6, 7]
# lgst=l[0]
# for i in l:
#     if i >lgst:
#         lgst=i
# print(lgst)

# # remove duplicates
# l=[2,2,2,3,4,5,5,1,2]
# u=[]
# for item in l:
#     if item not in u:
#         u.append(item)
# print(u)

#prime or not

# def prime(n):
    
#     for i in range (2,n):
#         if n%i==0:
#             return False
#     return True


# print(prime(15))

    

# def fib(n):
#     if n<=1:
#         return 1
#     return fib(n-1)+fib(n-2)
# n=int(input("enter the value of n"))
# for i in range(n):
#     print(fib(n))



class Math:
    def add(self, a, b, c=0):
        # if c is None:
        #     return a + b
        # else:
            return a + b + c

m = Math()
print(m.add(2, 3))      # 2 args
# print(m.add(2, 3, 4))   # 3 args
