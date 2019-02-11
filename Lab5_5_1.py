class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print_point(self):
        print "x =", self.x, ",",
        print "y =", self.y

point = Point()
point.print_point()

point = Point(10)
point.print_point()

point = Point(20, 30)
point.print_point()

#String method
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

point = Point()
print point

point = Point(10)
print point

point = Point(10, 15)
print point
#third part
class Point(object):
    def __init__ (self, x = 0, y = 0):
        self.x = x
        self.y = y
         
    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)
         
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_point = Point(new_x, new_y)
        return new_point
         
point1 = Point(1, 3)
point2 = Point(4, 5)
 
print point1 + point2