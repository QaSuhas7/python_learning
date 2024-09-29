s="WelCome"
for i in s:
    print(i) ##op--> here code will print each word in string

##Tetsing Strings
"""s="1manShow"
print(s.isalnum()) #op--> True
d="man"
print(d.isalpha()) #op--> True
f="647"
print(f.isdigit()) #op--> True
h="Welcome"
print(h.isidentifier()) #op--> True
j="To"
print(j.islower()) #op--> False
k="TRUE"
print(k.isupper()) #op--> True
print(" ".isspace()) #op--> True"""

#Searching functions in string
print("-------------------------------------------")
s="Welcome in my python world"
print(s.endswith("rld"))
print(s.startswith("Welcome"))
print(s.count("o"))
print(s.find("p"))
print(s.rfind("o"))
print("--------------------------------------------")

#Converting function
s="Welcome in JUNGLE"
print(s.capitalize()) #op-->Welcome in jungle
print(s.lower()) #op-->Welcome in jungle
print(s.upper())#op-->WELCOME IN JUNGLE
print(s.title())#op-->Welcome In Jungle
print(s.swapcase())#op-->wELCOME IN jungle
print(s.replace("JUNGLE","Python"))#op-->Welcome in Python



