from math import pow, sqrt

class Point:
    """A 2D point in space"""

    def __init__(self, x, y): #Constructor
        """Create a point"""
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        """Return the string representation of a point"""
        #print("Point __str__ called")
        return "(%f, %f)" %(self.x, self.y)

    def move(self, x, y):
        """Move a point by x units along x-axis and y units along y-axis"""
        self.x += float(x)
        self.y += float(y)

    def distance(self, other):
        if not isinstance(other, Point): raise TypeError
        xdif = self.x - other.x
        ydif = self.y - other.y
        return sqrt(pow(xdif, 2) + pow(ydif, 2))

class Rectangle:
    """A 2D rectangle in space"""

    def __init__(self, lbp, rtp):
        """A rectangle defined by two points:
        1) left bottom point
        2) right top point"""
        if not isinstance(lbp, Point): raise TypeError
        if not isinstance(rtp, Point): raise TypeError
        self.lbp = lbp
        self.rtp = rtp

    def __str__(self):
        """Return the string representation of the rectangle
        """
        return "[" + str(self.lbp) + "," + str(self.rtp) + "]"

    def width(self):
        """Return the width of the rectangle"""
        return abs(self.rtp.x - self.lbp.x)

    def height(self):
        """Return the width of the rectangle"""
        return abs(self.rtp.y - self.lbp.y)

    def area(self):
        """Return the area of  the rectangle"""
        return self.width() * self.height()

    def move(self, x, y):
        """Move a rectangle by x units along x-axis and y units along y-axis"""
        self.lbp.move(x, y)
        self.rtp.move(x, y)

if __name__ == '__main__':
    pt1 = Point(1, 2)
    pt2 = Point(1, 4)
    print('Point 1 = ' + str(pt1))
    print('Point 2 = ' + str(pt2))
    print('Distance before move = ' + str(pt1.distance(pt2)))
    pt1.move(0, 1)
    print('Distance after move = ' + str(pt1.distance(pt2)))
    print(pt1.distance(pt2))
    print('Distance of a point with itself = ' + str(pt1.distance(pt1)))

    pt3 = Point(0, 0)
    pt4 = Point(3, 4)
    rct1 = Rectangle(pt3, pt4)
    print(rct1)
    print('Width = ' + str(rct1.width()))
    print('Height = ' + str(rct1.height()))
    rct1.move(4, 3)
    print("After move " + str(rct1))
    print("Aread = " + str(rct1.area()))

