# Three types of methods
# # 1. Instance method
#     - Accessor (fetching value )
#     - Mutator
# 2. Class Methods
# 3. Static Methods


class Student:

    studentName= "Emrul";

    def __init__(self,mark1,mark2,mark3):
        self.mark1=mark1;
        self.mark2=mark2;
        self.mark3=mark3;
    #instance method
    def avg(self):
        avg=self.mark1+self.mark2+self.mark3/3;
        return avg;

    # accessor
    def getMark1(self):
        return self.mark1;

    # mutator
    def setMark1(self,mark1):
        self.mark1=mark1;

    #Class method
    @classmethod
    def getInfo(cls):
        return cls.studentName;
    #Static method
    @staticmethod
    def statInfo():
        return "This code is done by RONY";

studentObj= Student(50,60,65);

print("The name of the student is", Student.getInfo());

print("The average of three numbers are",studentObj.avg());

print("Getting mark1", studentObj.getMark1());

studentObj.setMark1(99);

print("Getting mark1 after setting it", studentObj.getMark1());

print(Student.statInfo());






