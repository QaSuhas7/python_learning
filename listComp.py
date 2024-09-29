#List comprehension
list1=[i for i in range(10)] # Here we are storing i continuously while adding values
print(list1) #--> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list2=[i+1 for i in range(10)]  # We are storing and subtracting the value from next upcoming value
print(list2)

list3=[i for i in range(20) if i%2==0] # Here we are printing i but if only i%2==0, it means i should be even number
print(list3)

list4=[i for i in range(20) if i%2==1]
print(list4)

