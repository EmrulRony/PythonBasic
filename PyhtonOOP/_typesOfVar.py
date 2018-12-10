# Two Types of variable
# 1. instance var
# 2. class var

class Car:

    age=26; #Class var

    def __init__(self):
        self.x=10;          #Instance var under __init():
        self.s="Rony";

obj = Car();
obj1= Car();

obj.x=100;

Car.age=25;

print(obj.x, obj.s, Car.age);
print(obj1.x,obj1.s, Car.age);
