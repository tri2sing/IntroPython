from Classes01 import Point, Rectangle

class Circle:
    """Represents a circle in 2D space"""

    def __init__(self, center, radius):
        """Creates a circle with given center point and radius"""
        if not isinstance(center, Point): raise TypeError
        if not isinstance(radius, float): raise TypeError
        self.center = center
        self.radius = float(radius)

    def __str__(self):
        """String representation of a circle"""
        return "Center = " + str(self.center) + " Radius = " + str(self.radius)

    def move(self, x, y):
        """Move a circle by x units along x-axis and y units along y-axis"""
        self.center.move(x, y)

    def boundingrectangle(self):
        """Return the rectangle whose side bound the circle"""
        x = float(self.center.x)
        y = float(self.center.y)
        r = float(self.radius)
        lbp = Point(x, y)
        lbp.move(-r, -r)
        print(lbp)
        rtp = Point(x, y)
        rtp.move(r, r)
        print(rtp)
        return Rectangle(lbp, rtp)

if __name__ == "__main__":
    cen = Point (5, 6)
    r = 5.5
    cir = Circle(cen, r)
    print(cir)
    rct = cir.boundingrectangle()
    print(rct)
