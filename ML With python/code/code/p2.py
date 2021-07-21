"""Create a class named 'Rectangle' with two data members 'length' and 'breadth' and two methods to print the area and perimeter of the rectangle respectively. Its constructor having parameters for length and breadth is used to initialize length and breadth of the rectangle. Let class 'Square' inherit the 'Rectangle' class with its constructor having a parameter for its side (suppose s) calling the constructor of its parent class as 'super(s,s)'. Print the area and perimeter of a rectangle and a square.
"""

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

r=Rectangle(2,3)
r.area()
r.parameter()
sq=Square(5)
sq.area()
sq.parameter()