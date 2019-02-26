# x = 40
# print(id(40))
# print(id(x))
# a = x
# x = 50
# print(id(a))
# print(id(x))

a = 40
print(a.__class__)

class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destroyed")


print(Point)

# pt1 = Point()
# pt2 = pt1
# pt3 = pt1
# print(pt1.__class__.__name__)


# print (id(pt1), id(pt2), id(pt3))   # prints the ids of the obejcts
# del pt1
# print (id(pt1), id(pt2), id(pt3))
# del pt2
# del pt3
