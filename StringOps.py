# Creating String
#Approch 1
name="Suhas"
fname='Suhas'
lname='G'

#Approch 2
name1 = str("Suhas")
print(id(name1))  # id() which will return memory location
print(id(name))
print(id(fname))
# Above all id function is returning same value because assigned value/String is same for all variable
print(id(lname))

## Operation on Strings
print(name+lname)  ## "+" Operator for concatenation of two strings. op-->SuhasG
print(name*2)      ## "*" Operator for repetition of String op-->SuhasSuhas

##Slicing in String
str ="Welcome"
print(str[1:3]) ##op--->el-- Here 1:3 its range it will print from 1 to n-1 (Where n is 3)
print(str[:7])  ##op--> Welcome ---before : nothing means 0th index
print(str[4:])  ##Op--->ome --it will print from 4 to end
## Basically in above code we are doing substring of string using indexing
print(len(str))  #op--->7 len method is showing how many character in string

##ord() and chr() functions
##ASCII code and number of character
print(ord('A'))  ##op--> 65 is ASCII number of "A"--- Accepting char value
print(chr(65))   ##op--> A is ASCII code of 65 number---Accepting int value

char ='A'
ascii_code=ord(char)
print(f"ASCII number of {char} is {ascii_code}")

num =66
ascii_num=chr(num)
print(f"ASCII code of {num} is {ascii_num}")
print("num:{},ascii_num:{}".format(num,ascii_num))
