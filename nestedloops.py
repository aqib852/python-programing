



# sum of series of factorials: 1! + 2! + 3! + ... + n!
# sum of series of factorials: 1! + 2! + 3! + ... + n!
# n = int(input("Enter a number: "))
# sum = 0

# for i in range(1, n+1):
#     fact = 1  # reset factorial for each i
#     for j in range(1, i+1):
#         fact *= j
#     sum += fact

# print("Sum of factorial series =", sum)



#without using nested loops


# n = int(input("Enter a number: "))
# sum=0
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
#     sum=sum+fact
# print(sum)





# sum of inverse of a factorial series

# n = int(input("Enter a number: "))
# sum = 0
# # sign=1
# for i in range(1, n+1):
#     fact = 1  # reset factorial for each i
#     for j in range(1, i+1):
#         fact *= j
#         # inverse_fact=1/fact
    
#     sum = sum+1/fact
#     # sign=sign*-1

# print("Sum of factorial series =", sum)

# inverted traingle
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# inverted traingle of numbers
# for i in range(6,0,-1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

#pyramid
# for i in range(1, 6):
#     for s in range(5-i):
#         print(" ", end=" ")
#     for j in range(2*i-1):
#         print("*", end=" ")
#     print()

# pascals traingle
# n = 5
# for i in range(n):
#     num = 1
#     for space in range(n-i-1):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print(num, end=" ")
#         num = num * (i - j) // (j + 1)
#     print()



#pyramid
# n=4
# for i in range(1, n+1):
#     print(" "*(n-i), end="")
#     print("* " * i)


# armstrong number
# n=int(input("enter a number"))
# sn=str(n)
# lsn=len(sn)
# sum=0
# temp=n
# for i in range(0,n+1):
#     d=n%10
#     sum=sum+d**lsn
#     n=n//10
# if n == sum:
#     print("arm")
# else:
#     print("not arm")


# vowel in a nmbr
# n = input("Enter a string: ")

# for ch in n:
#     if ch in "aeiouAEIOU":
#         print(ch,end=" ")
       
#     else:
#         print(ch,end=" ")




# n=6
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*i)

# n=5
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("* "*i)


       

