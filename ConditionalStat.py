a=30

if a>20:
    print("True Condition")
else:
    print("False Condition")

#-------------------------------------------
if False:
    print("True Condition")
else:
    print("False Condition")
#----------------------------------------
if 0:
    print("Yes")
else:
    print("No")
#--------------------------------------
#Print number is even or odd number
x=15

if x%2==0:
    print("Number is even number")
else:
    print("Number is odd number")
#-------------------------------------
#Multiple statements under if else block
if False:
    print("Statement1")
    print("Statement2")
    print("Statement3")
else:
    print("Statement4")
    print("Statement5")
print("This is not the part of if and else block")

#Single line in single line
print("Hello world") if True else print("Hello Pune")  #--> Boolean value
print("Hello world") if a>4 else print("Hello pune")   #---> Conditions

#Multiple statement in single line
{print("Hello world python"), print("Hi World")} if False else {print("Welcome to world"),print("Welcome to pune")}



