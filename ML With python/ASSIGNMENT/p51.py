class Student:
 def setvalue(self,rollno,name,fee):
  self.rn=rollno
  self.n=name
  self.f=fee
 def display(self):
  print("Student roll number is : ",self.rn)
  print("Student name is :",self.n)
  print("Student fee is :",self.f)
s=Student()
rn=int(input("Plese Enter the student roll number"))
n=input("plese enter student name")
f=int(input("Plese Enter the student Fee"))
s.setvalue(rn,n,f)
s.display()
