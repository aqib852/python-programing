class animal:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    #getter
    def get_name(self):
        return self.__name
    #setter
    def set_age(self):
        return self.__age + 32
o1= animal("aqib",30)
print(o1.set_age())
    
