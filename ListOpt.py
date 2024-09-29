#List Common operations
from itertools import count
from operator import index

#Append command
s=[22,4,556,74,43,22]
s.append(1) # it will append the value
print(s) #op--> 22,4,556,74,43,1
print((s.count(22))) # op-->2
s2=[1,3]
s.extend(s2)
print(s) #[22,4,556,74,43,22,1,3] here we extended the list
print(s.index(22)) #op--> parameter is value not index
s.insert(2,45)
print(s)
print(s.pop(4))# in this function it will return the element and along with it remove from list
print(s)
s.remove(22) # parameter should be a value, it will remove that value from list
print(s)
s.sort() # It will sort the list element in Ascending order
print(s)
s.reverse() # It will reverse the list element
print(s)



