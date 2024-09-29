# Break command
for i in range(1,10):
    if i==6:
        print(i)
        break
        # Op---> 6

for a in range(1,10):
    if a==5:
        break
    print(a) #--------Indentation is imp
        # op--> 1,2,3,4,5

#Continue
for i in range(1,10):
    if i==6:
        continue
    print(i)
else:
    print("Number is not in range")