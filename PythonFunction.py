#How to create a function
"""def sumo(start, end):
    result =0
    for i in range(start,end+1):
        result=result+i
    print(result)
#How to use the function
sumo(10,20)

def compare(start,end):
    if start>end:
        print("Start",start ,"is bigger value than",end,"end")
    else:
        print(f"Start{start} is not greeter that end {end} value ")
       # print("Start",start," is not bigger than end",end ,"value")


compare(4,45)
"""

#Local & Global variable
s=12  #This is global variable we can access this inside/ the function.
def myname():
    g=11   # This is the local function we can access this only in the function.
    print(s+g)
myname()

def increment():
    global s
    s=10  ## We are modefing the global variable values
    print(s)
increment()

print("---------------------------")
#passing arguments with default values (Optional)
def val(i,j=22):  # value for j is assigned by default.
    print(i,j)
val(20)

#Keyword arguments
def named_args(name, greeting):
     print(greeting+ " " +name )

named_args("My", "name")
named_args(greeting="Let",name="Me")

#Mixing od positional and keywords
def numv(a,b,c):
    print(a,b,c)
numv(11,23,44) #Optional parameters
numv(1,b=22,c=77) #Keyword parameter, we can not pass positional arg after a keyword args
numv(b=3,c=9,a=3) #mixed parameter (No order required
print("----------------------------------------")
# Return multiple values from function
def big(a,b):
    if a>b:
        return a,b
    else:
        return b,a

t=big(11,34)  # Return values treat as tuple
print(t)
print(type(t))















