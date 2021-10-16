class Person(object):

    def __init__(self) -> None:
        self.name = 'Pagla Arman'
        self.age = 12

    def __str__(self) -> str:
        return self.name

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


# p1 = Person()
# print(p1)    
p1 = Person()
print(p1.getName())  
print(p1.getAge())  

