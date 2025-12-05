# map() and filter() in Python
L=[1,2,3,4,5,6]
result = map(lambda x: x * 2, numbers)

print(list(result)) 
#example 2
def square(x):
    return x * x

numbers = [1, 2, 3, 4]
result = map(square, numbers)

print(list(result))   # [1, 4, 9, 16]

#filter
numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))   # [2, 4, 6]

