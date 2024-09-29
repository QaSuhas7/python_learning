#how to declare tuple
t1=() #empty
t2=(1,2,4,5,6) #(1, 2, 4, 5, 6)
t3=([1,2,3,4,5,6]) #[1, 2, 3, 4, 5, 6]
t4=tuple("Suhas") #('S', 'u', 'h', 'a', 's')
print(t4)
print(t1)
print(t2)
print(t3)

#Tuple functions
print(min(t2)) #Smallest value
print(max(t2))  # Max value
print(sum(t2)) # sum of values
print(len(t2)) #len of values
print("---------------------------------")
#Iteration on tuple
for i in t2:
    print(i) # end= parameter give the all values in same line

print("----------------------------")
#scilcing
print(t2[2:4])
print(t2[1:3])

#In and not in operator
print(1 in t2)
print(33 not in t2)
