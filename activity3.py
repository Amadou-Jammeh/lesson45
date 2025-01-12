class Parrot:
    #class variable
    species="Bird"

    def __init__(self,name,age):
        #instance variables
        self.name=name
        self.age=age

p1=Parrot("Rio",2)
p2=Parrot("Blu",3)

print(p1.name,"is a",p1.species)
print(p2.name,"is a",p2.species)

print(p1.name,"is",p1.age,"year old")
print(p2.name,"is",p2.age,"year old")
