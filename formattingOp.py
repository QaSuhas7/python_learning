name = "John"
age= 25
sal=200.5

#Formatting Approach1
print(name,age,sal)
#Formatting Approach2
print("Name:",name)
print("Age:",age)
print("Salary:",sal)
#Formatting Approach3---->Using % operator, Here type of data is very IMP
print("Name is:%s Age:%d Salary:%g"%(name,age,sal))

#Formatting Approach4
print("Name:{}  Age:{}  Salary:{}".format(name,age,sal)) #----> Value of variable is very imp

#Formatting Approach5
print("Name:{0} Age:{1} Salary:{2}".format(name,age,sal))  #---> remember index is starting from "0" only which IP




