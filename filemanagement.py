file=open("tops1.txt","w")
file.write("This istops 1 file")
file.close()
print("File written successfully")

print("*"*50)

file=open("tops1.txt","r")
print(file.read())
file.close()

print("*"*50)

file=open("tops1.txt","a")
file.write("This istops 1 file is appended")
file.close()
print("File appended successfully")

print("*"*50)

file=open("tops2.txt","w+")
file.write("This istops 2 file")
print("Current position of cursor",file.tell())
file.seek(0)
print("File data :",file.read())
file.close()
