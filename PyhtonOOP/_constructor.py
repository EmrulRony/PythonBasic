class MyConst:
    def __init__(self,x,y):
        self.x=x;
        self.y=y;
        z = x + y
        print("This is a const",z);
    def myMet(self,str):
        self.str=str;
        print(str);


obj = MyConst(2,3);
obj2 = MyConst(2,3);

obj.myMet("My Name is Khan")
