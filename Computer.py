class Computer:
    def __init__(self):
        print("inside non-argumented __init__");

    def __init__(self,x,y):
        self.x=x;
        self.y=y;
        print("inside argumented __int__")
        print(x+y);

    def config(self):
        print("15,16gb,1TB", self.x);

# a ='8';

compObj2 = Computer(5,6);
compObj = Computer(10,20);

#
# print(type(a));
# print(type(compObj));

compObj.config();
compObj2.config();

