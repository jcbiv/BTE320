class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff = (self.x - other.x)**2
        y_diff = (self.y - other.y)**2

        d = (x_diff+y_diff)**0.5
        return d

class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    
    def distance3D(self, other):
        z_diff = (self.z - other.z)**2
        x_diff = (self.x - other.x)**2
        y_diff = (self.y - other.y)**2

        d = (x_diff+y_diff+z_diff)**0.5
        return d
    
p1 = Point3D(234,645,11)
p2 = Point3D(754,382,683)

print(p1.distance3D(p2))

