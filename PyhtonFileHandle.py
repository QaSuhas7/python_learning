#How to open file
f = open('C:/Users/sghodake/Desktop/Python/myData.txt','w') # Where 'w' is for write mode
#How to write the file
f.write("This is first line\n")
f.write("This is a second line\n")
f.write("This is a third line\n")
f.write("This is a fourth line\n")
f.write("This is a five line\n")
f.write("This is a six line\n")
f.write("This is a seven line\n")
f.write("This is a eight line\n")
f.write("This is a nine line\n")
f.write("This is a ten line\n")
f.close()  #We are closing the file
#how to read the file
"""read = open('C:/Users/sghodake/Desktop/Python/myData.txt','r') # Where 'r' is for read mode
print(read.read()) # It will return that number of character
read.close()"""

# Read file using for loop
file= open('C:/Users/sghodake/Desktop/Python/myData.txt','r')

for l in file:
    print(f"",l)

file.close()





