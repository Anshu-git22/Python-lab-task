d={1:"Anshu",2:"Raj",3:"Parit"}
key=int(input("Enter Existing Key:"))
value=input("Enter new value:")

if key in d:
    d[key]=value
else:
    print("Key is not Presented")

print(d)
