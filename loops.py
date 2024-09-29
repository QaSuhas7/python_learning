#Befor starting loops (for) we need to look into range function
"""print(list(range(10)))  #--> Op-[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,10,3))) #-->[1, 4, 7]
print(list(range(-10,-5,2))) #--> [-10, -8, -6]
print(list(range(10,1,-2)))"""  #--> [10, 8, 6, 4, 2] here range is 10 to 1 and decrement by 2 (- Decrement,+ Increment)

#For Loop----------------------------------------------------------------
#Print 1 to 10 numbers
# for i in range(10): # i is starting from 0 by default
#     print(i)

#pint odd numbers in 1 to 10
# for i in range(1,10,2):
#     print(i)  #-->Op-1,3,5,7,9
#Explanation on above snipped
#1 is starting position 10 is last position means 1 to 10 is range and 2 is incremental value/Decremental value

#pint even numbers in 1 to 10
# for i in range(2,10,2):
#     print(i)  #-->Op-2,4,6,8


#While loop-----------------------------------------------------------

i=1   #We declare i here
while i<=10:   # Here we have condition
    print(i)         #printing statement
    i=i+1      #Increment of i
print("------------------10 to 1 descending number----------------------")
i=10
while i>=1:
    print(i)
    i=i-1