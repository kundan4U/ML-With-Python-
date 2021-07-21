class Rectangle:
 def __init__(self,length,breadth):
  self.length=length
  self.breadth=breadth
 def area(self):
  print("Area of he Ractangle is       :",(self.length*self.breadth))
 def perimeter(self):
  print("Perimeter of the Ractangle is :",2(self.length+self.breadth))
class Squre(Ractangle):
 def __init__(self,s):
  super().__init__(s,s)
r=Ractangle(2,3)
r.area()
r.perimeter()
sq=Squre(5)
sq.area()
sq.perimeter()
