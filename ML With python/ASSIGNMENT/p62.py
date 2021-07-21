class Rectangle:
 def __init__(self,length,breadth):
  self.length=length
  self.breadth=breadth
 def area(self):
  print("Area of Rectangle = ",(self.length*self.breadth))
 def parameter(self):
  print("Paremeter of Rectangle = ",(2*(self.length*self.breadth)))
class Square(Rectangle):
 def __init__(self,s):
  super().__init__(s,s)
r=Rectangle(5,3)
r.area()
r.parameter()
sq=Square(9)
sq.area()
sq.parameter()