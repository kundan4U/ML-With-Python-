class Shape:
 def print_shape(self):
  print("This is shape")
class Rectangle(Shape):
 def print_rect(self):
  print("This is rectangular shape")
class Circle(Shape):
 def print_circle(self):
  print("This is circular shape")
class Square(Rectangle):
 def print_square(self):
  print("Square is a rectangle")
sq=Square()
sq.print_shape()
sq.print_rect()