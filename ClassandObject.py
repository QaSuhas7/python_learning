class MyClass:
    def myfunction(self): #instance method
        pass
    def display(self,name): # self is notifying like this function is belong from this function
        print(name)
    @staticmethod
    def mymethod(surname):  #This is a static method
        print(surname)

   #Diff between function and method
   #within class----method
   #out of the class ---function
mc=MyClass()
mc.myfunction()
mc.display("Madhavi Suhas Ghodake")
MyClass.mymethod("This is static method")


