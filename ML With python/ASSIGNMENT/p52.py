class Interest:
 def __init__(self,p,n,r):
  self.p=p
  self.n=n
  self.r=r
 def simpleinterest(self):
  print("Simple Interest is  :",(self.p*self.r*self.n)/100)
x=int(input("Plese Enter Principil Amount :" ))
y=int(input("Plese Enter Interest rate : "))
z=int(input("Plese Enter Number of time : "))
s=Interest(x,y,z)
s.simpleinterest()