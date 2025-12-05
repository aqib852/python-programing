s=set()
n = int(input("enter number: "))
s.add((n))
n = int(input("enter number: "))
s.add((n))
n = int(input("enter number: "))
s.add((n))
n = int(input("enter number: "))
s.add((n))
print(s)


s2 =set()
s2.add((18))
s2.add(("18"))
s2.add((18.0))    # 18.0 = 18   bcz  data type doesnt matter when values are same for int and float

print(s2)
print(len(s2)) #length = 2


friends = {}

n1 = input("enter your name ")
l1 = input("and your fav language")
friends.update({n1:l1})
n2 = input("enter your name ")
l2 = input("and your fav language")
friends.update({n2:l2})
n3 = input("enter your name")
l3 = input("your fav language")
friends.update({n3:l3})
n4 = input("enter your name")
l4 =input(" enter your fav language")
friends.update({n4:l4})
print(friends)
 
