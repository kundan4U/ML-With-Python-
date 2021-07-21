class Rectangle:
 def __init__(self,length,width):
  self.l=length
  self.w=width
 def rectArea(self):
  return self.l*self.w
 def rectPeri(self):
  return 2*(self.l+self.w)
x=int(input("Plese Enter the length of Ractangle : "))
y=int(input("Plese Enter the width of Ractangle : "))
r=Rectangle(x,y)
print("Area of Rectangle is :",r.rectArea())
print("Perimeter of Rectangle is :",r.rectPeri())
  