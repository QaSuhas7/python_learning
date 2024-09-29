'''num=input("Enter the first number:")  # treated as String
num2=input("Enter the second number:")  # Treated as String
print(num+num2) # It should concatenation of above two variables'''

# How we can get user input in diff datatype
# We need to do typecasting
n=int(input("Enter the first number:"))  # treated as String
n2=int(input("Enter the second number:")) # Treated as String

print(n+n2)

##Float
a=float(input("Enter float number:")) #--->1.3
b=float(input("Enter float number:"))  #--->1.2
print(a+b)  #----------> O/P should be 2.5

print(n+a) #--->ValueError: invalid literal for int() with base 10: '1.2' integer can not hold float variable/value


