# This program demonstrate inner class in Python

# outer class
class Student:
    def __init__(self,sName,sId):
        self.sName=sName;
        self.sId=sId;
        self.laptop=self.Laptop();


    def getStudentInfo(self):
        print(self.sName," ", self.sId);

    # inner class
    class Laptop:

        def __init__(self):
            self.brand="";
            self.ram=0;
        def setLapInfo(self,brand,ram):
            self.brand=brand;
            self.ram=ram;
        def getLapInfo(self):
            print(self.brand," ",self.ram);

objStudent = Student("Emrul",104);
objStudent.getStudentInfo();
objStudent.laptop.setLapInfo("Asus",6);
objStudent.laptop.getLapInfo();

objStudent1= Student("Rony",105);
objStudent1.getStudentInfo();
objStudent1.laptop.setLapInfo("Dell",8);
objStudent1.laptop.getLapInfo();

print("---------Creating laptop obj---------");

lapObj = objStudent.laptop
lapObj.getLapInfo();
lapObj.setLapInfo("Doel",16);
lapObj.getLapInfo();
