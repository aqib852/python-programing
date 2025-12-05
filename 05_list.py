# friends=["jamid","aqib","anayat","gowhar","90"] # can store multiple date types

# print(friends[2])

# friends[2]= "naveed"   #unlike strings lists are mutable we can change the valeue of list but the strings is not changed

# print(friends[2])

# print(friends[0:2])     # slicing is possible in lists also 

# print(friends[0:4:2])   #slice with skip value 



#list method

# friends.append("sajid")

# print(friends)
# friends[2]="anayat"

# L=["1","20","jam","1.20","aqii"] #sorting is only possibe when we have simmiller type of data as here is all strings
# L.sort()
# print(L)
# L.reverse()
# print(L)
# L.insert(2,30)
# print(L)
#LARGERST NUMBER IN THE LIST
L=[12,2,43,45,60,90,28]
largest=L[0]
# unique=[]
for item in L:
    if item > largest:

    #    unique.append(item)
        largest = item
print(largest)

#number of even numbers in a list

L=[12,2,43,45,60,90,28]
count=0
for item in L:
    if item%2==0:
        count=count+1
print(count)

#sum of all the elements in a list

L=[12,2,43,45,60,90,28]
sum=0
for item in L:
    sum=sum+item
print(sum)

# reverse a list without using inbuilt function
L=[12,2,43,45,60,90,28]
L.reverse()
print(L)

c=len(L)
L_r=[]
for item in L:
    L_r.append(L[c-1])
    c=c-1
print(L_r)

#copy all the elements of a list using loops
L=[12,2,43,45,60,90,28]
# ml=[]
# ml.extend(L)# we can copy using extend inbuilt function
# print(ml)
nl=[]
for item in L:
    nl.append(item)
print(nl)

#nested lists print sum of two matrices
L1=[[1,2,4,5],[6,4,2,6],[6,8,6,9]]
L2=[[1,2,4,5],[6,4,2,6],[6,8,6,9]]


L3=[]


for i in range(len(L1)):
    
    n=[]
    
    for j in range(len(L1[0])):
         n.append(L1[i][j]+L2[i][j])
    L3.append(n)
    

print(L3)
#nested lists product of two matricies
L1=[[1,2,4],[6,4,2],[6,8,6]]
L2=[[1,2,4],[6,4,2],[6,8,6]]
L3=[]

for i in range(0,3):
    row=[]
    # j=0
    # k=0
    # l=0
    # m=0

    for j in range(len(L2[0])):
        # n.append(L1[i][j]*L2[i][j]+L1[i][j+1]* L2[i+1][j]+L1[i][j+2]*L2[i+2][j])
        s=0
        for k in range(0,3):
            s=s+L1[i][k]*L2[k][j]

        row.append(s)
    L3.append(row)
        

        
        
    

print(L3)



        

