class Point(object):
    """Represents a point in 2-D space."""

class Rectangle(object):
    """Represents a rectangle. 

    attributes: width, height, corner.
    """


import math
from swampy.Lumpy import Lumpy

a=Point()
b=Point()
a.x=0
a.y=0
b.x=4
b.y=4
r=Rectangle()
r.width=2
r.height=1
r.corner=a
dx=5
dy=7

def distance(a,b):
    """Takes two points, a and b. Returns distance between them (float)."""
    
    x_diff=a.x-b.x
    y_diff=a.y-b.y
    dist_sqd=abs(x_diff**2+y_diff**2)
    dist=math.sqrt(dist_sqd)
    return dist


def move_rect(r, dx, dy):
    """Takes a rectangle, r, and returns a new rectangle which has been shifted dx units in the x direction and dy units in the y direction. dx and dy should be numbers."""
    corner=r.corner
    corner.x=corner.x+dx
    corner.y=corner.y+dy
    r.corner=corner
    return r


def move_rect_2(r, dx, dy):
    """Takes a rectangle, r, and returns a new rectangle which has been shifted dx units in the x direction and dy units in the y direction. dx and dy should be numbers."""
    new_r=Rectangle()
    new_corner=Point()
    corner=r.corner
    new_corner.x=corner.x+dx
    new_corner.y=corner.y+dy
    new_r.corner=new_corner
    new_r.width=r.width
    new_r.height=r.height
    
    return new_r


if __name__ == "__main__":
    lumpy=Lumpy()
    print distance(a,b)
    new_rect=move_rect_2(r,dx,dy)
    new_corner=new_rect.corner
    print new_corner.x
    print new_corner.y
    print new_rect.width
    print new_rect.height
    lumpy.object_diagram()
