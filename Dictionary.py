d={101:"Anshu",201:"Parit",301:"Arpit",401:"Rushank",501:"Shivraj",601:"Raj"}

print(d)
print(d[201])
print(d.get(201))
print(d.items())
print(d.keys())
print(d.pop(401))
print(d)
d.popitem()
print(d)
d1={701:"Shivani",801:"Vraj"}
d.update(d1)
print(d)
print(d.values())

for i in d:
    print(i," : ",d[i])

for key,value in d.items():
    print(key," : ",value)

if 301 in d:
    print("Is Available")
else:
    print("Is not Available")
