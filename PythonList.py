a = list() # This is empty list
print(a)

b=list([12,45,65,66]) # int elements added
print(b)

c= list(['Suhas',"Madhavi","Chaitan"]) #String elements added
print(c)

d= list("Python") # Without [] its taking character
print(d)

for i in b:
    if i>=23:
        print(i)
    else:
        print("i is not greater than:",i)

print("--------------------------------")
#How we can access elements in list
#--> Lis is based on indexing, and we access elements using
#--> In the list indexing is starting from '0'

"""l=list([1,2,3,4,5])
print(l[0]) #op--> 1
#print(l[5]) # if specified indexing is not in the list, it will trow IndexError: list index out of range
print(l[4]) #op--> 5"""
print("_______________Comman operations_________________")

"""list1=[22,44,5,55,3,33]
list2=[2,4,5,54,3,33]
print(22 in list1) # True
print(33 not in list1)
print(list1+list2)
print(list1*3)
for i in list2:
    print(i,",")   # i th element in list
print(len(list1))
print(min(list2))
print(max(list1))
print(sum(list1))"""
print("-----------------List Slicing-------------")

s=[22,4,6,788,97,88]
s2=[11,56]
print(s[0:4]) # start from 0 and print upto n-1 ie. from o to 4-1
print(s[:3]) # Print from 0 (If we are not giving starting value)
print(s[2:])  # Print from 2 to at end of index, we did not give any last index.

print("---------------------+ and * Operators----------")
print(s+s2)
print(s2*3)
