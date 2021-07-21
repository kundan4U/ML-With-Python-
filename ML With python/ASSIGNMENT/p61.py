class A:
 def sum(self,a,b):
  return(a+b)
class B(A):
 def sub(self,a,b):
  return(a-b)
 def mul(self,a,b):
  return(a*b)
x=int(input("Plese enter first number      : "))
y=int(input("Plese Enter the second number :"))
I=B()
print("Sum of given number is is     :",I.sum(x,y))
print("Substration of given number  is : ",I.sub(x,y))
print("Multiplication of given number  is : ",I.mul(x,y))
  