#function with no argument & no return values.

def printline():
    print("*"*50)
printline()
print("Welcome To Userdefine Function in Python.")
printline()

#function with argument & no return values.

def add(a,b):
    print("Addition is:",a+b)
printline()
add(10,20)
printline()

#function with argument & return values.

def sub(a,b):
    return a-b
printline()
ans=sub(10,20)
print("Substraction is :",ans)
printline()
