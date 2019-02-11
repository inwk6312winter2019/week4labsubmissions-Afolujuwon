import math
class Point():
	def __init__(self,p1,p2):
		self.p1 = p1
		self.p2 = p2

	def distance_between_point(self):
		x1,y1 = self.p1
		x2,y2 = self.p2

		delta_y = y2 - y1
		delta_x = x2 - x1
		distance = math.sqrt((delta_y)**2 + (delta_x)**2)
		return distance



class Rectangle():
	#def __init__(self,width,height,corner)
	def __init__(self,width,height,corner):
		self.width = width
		self.height = height
		self.corner = (0,0)

	def find_center(self):
		object1 = Point((0,0),(0,100))
		dy = object1.distance_between_point() / 2
		object2 = Point((0,0),(200,0))
		dx = object2.distance_between_point() / 2
		print('(', dx,',', dy,')' )

box = Rectangle(200,100,(0,0))

box.find_center()

