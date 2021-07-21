"""
Create a class named 'Shape' with a method to print " This is shape". Then create two other classes named 'Rectangle', 'Circle' inheriting the Shape class, both having a method to print "This is rectangular shape" and "This is circular shape" respectively. Create a subclass 'Square' of 'Rectangle' having a method to print "Square is a rectangle". Now call the method of 'Shape' and 'Rectangle' class by the object of 'Square' class.
"""
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