from math import pi

class Circle:
	def __init__(self, radius):
		self.radius = radius
	def area(self):
		return pi * (self.radius**2)
circle1 = Circle(6)
print(circle1.area())
