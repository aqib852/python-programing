dictionary is because of fast lookup
name = {
    "jamid":"fayaz",
      "aqib" : "yousuf",
      "anayat":"shupain",
      }
print(name)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(type(thisdict))
print(thisdict.get("model"))
# thisdict.pop("year")
del thisdict["model"]

print(thisdict.update({"model" : "ferrari"}))
copy = thisdict.copy()
print(copy)

mydict = dict(copy)
print(mydict)

# nested dictionary
myfamily = {
    "child1" : {
        "name" : "aqib",
        "age" :  24
    },
    "child2" : {
        "name" : "sajid",
        "age" : 27
    }
}
print(myfamily)
print(myfamily.items())

# the differnece is if we execute whole code stops in simple
# print(myfamily.get("child2")) #print none

# print(myfamily) # prints error

#it unordered 
# unindexed
# immutable
num_dict = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

# Input from user
num = input("Enter a number: ")
output = " ".join(num_dict[d] for d in num)

# print(output)
message=input(">")
word=message.split(' ')
print(word)
