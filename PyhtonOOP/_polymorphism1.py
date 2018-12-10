# -----------Operator overloading------------
# We have already seen you can use +  operator for adding numbers and at the same time to concatenate strings.
# It is possible because +  operator is overloaded by both int class and str  class.
# The operators are actually methods defined in respective classes. Defining methods for operators is known as operator overloading.
# For e.g. To use +  operator with custom objects you need to define a method called_add.
import math
class Circle:

    def __init__(self,radius):
        self.radius = radius;
    # def setRad(self,radius):
    #     self.radius=radius;

    def getRad(self):

        return self.radius;

    def cArea(self):

        return math.pi*self.radius**2

    def __add__(self, other):
        return Circle(self.radius+other.radius)

    def __str__(self):
        return self.radius

#-----Circle 1-------

circle1 = Circle(5)
print("The radius of the circle 1 is",circle1.getRad())
print("The area of the circle 1 is", circle1.cArea())
#---------Circle2-----------

circle2 = Circle(10)
print("The radius of the circle 2 is",circle2.getRad())
print("The area of the circle 2 is", circle2.cArea())

sumC = circle1+circle2;

print("The sum of the two rad", sumC.__str__())





