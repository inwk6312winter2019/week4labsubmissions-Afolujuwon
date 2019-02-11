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
		print(distance)


object = Point((10,20),(20,30))
object.distance_between_point()


