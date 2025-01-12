class student:
    #class variables
    grade=10
    name="Amadou"
    def show(self):
        print("welcome to my first class method")
    def display(self):
        print("namw of the student is",self.name,"and grade is",self.grade)
st1=student()
st1.show()
st1.display()            