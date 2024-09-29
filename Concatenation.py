x=100   #---int type
j=200
y=10.5  #---float type

#  2) String/Char type
s="Suhas" #---String type
d='a'     # ---Char type

#   3) Boolean type
f= False
t= True

# Concatenation in python
# We can concatenate two same datatype, but we can not concatenate tow diff datatypes
# For ex
print(x+j) # Op should be 300 --------------Valid case
#print(x+s) # Op should be error ------------Invalid case (TypeError: unsupported operand type(s) for +: 'int' and 'str')
print(t+x) # Valid case  # Value of true is 1
print("Suhas"+ " Ghodake") # Valid case
print(False+True)