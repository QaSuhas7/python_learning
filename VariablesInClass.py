#Class variables
"""class MyClass:
    a=10    # Here a & b are class variables
    b=12
    def myFunc(self):
        print(self.a) # We can access variables using self keyword
    def mult(self):
        print(self.a*self.b)

m=MyClass()
m.myFunc()
m.mult()"""

c,d=1,2      ### Those are the global variable
class MyClass:
    a,b=10,20   ### Those are the class variables
    def add(self, x,y):    ## Here x and y are local variable
        print(self.a*x)    # Accessing class variable need to use self parameter in class
        print(c*y)        ##We can access global variable directly

m=MyClass()
m.add(11,5)

#If you have same name of global variable

class MyName:
    def life(self,c,d):
        print(c*globals()['c'])

m1=MyName()
m1.life(5,3)



