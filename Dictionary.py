#How to create dictionary in python
dic={"Tom":22,'jack':32} # Here we have key as in "" and value is after :
print(dic) #{'Tom': 22, 'jack': 32}

# Retrieving, modifying and adding element in dictionary

#Retrieving
print(dic["Tom"]) # We need to add exact key

#Adding the element
dic['Sam']=443
print(dic)

#Modify Element
dic['Sam']=5
print(dic)

#Deleting the element
del dic["Tom"]
print(dic)

dic["ram"]=544
print(dic)

#Looping in dic
for key in dic:
    if key=='Sam':
        print(key,":",dic[key]) # op--> Sam:5 ---Print key for given value

for key, i in dic.items():
    if i==5:
        print(i,":",key) #op--> 5:Sam  --Print value for given key
#How to find how many elements we have in dictionary
print(len(dic))

#Equality test in dictionary
d1={"mike":34,"rob":64}
d2={"rob":64,"mike":34}
print(d1==d2) #-->True, Order is not important but element should present in dic with same values.
print(d1!=d2) #-->False
