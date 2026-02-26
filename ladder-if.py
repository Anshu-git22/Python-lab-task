rno=int(input("Enter your roll no :"))
sname=input("Enter your name :")
s1=int(input("Enter mark of  subject1 :"))
s2=int(input("Enter mark of  subject2 :"))
s3=int(input("Enter mark of  subject3 :"))
total=s1+s2+s3
per=total/3

print("ROll no:",rno)
print("Student name:",sname)
print("Total:",total)
print("Persentage:",per)

if per>=70:
        print("Distintion")
elif per>=60:
     print("first class")
elif per>=50:
     print("Second class")
elif per>=40:
     print("Pass class")
else:
     print("Fail")
