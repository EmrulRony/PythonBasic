# types of inheritance in Python
# 1. Single level
# 2. Multi level inheritance
# 3. Multilevel inheritance
class Person:
    def __init__(self,firstName,lastName):
        self.firstName= firstName
        self.lastName=lastName
    def getName(self):
        strName= self.firstName+" "+self.lastName
        return strName

class Employee(Person):
    def __init__(self,firstName,lastName,empId,empPosition):
        super().__init__(firstName,lastName)
        self.empId=empId
        self.empPosition=empPosition

    def getEmpInfo(self):
        strInfo= self.firstName+" "+self.lastName+" "+str(self.empId)+" "+self.empPosition
        return strInfo

    # def printParent(self):
    #     print(self.firstName+" "+self.lastName);


# objPerson = Person("Emrul","Hasan");

objEmployee = Employee("Emrul","Hasan",104,"Engineer");

objEmployee1 = Employee("Jordan","Nakib",105,"Engineer");

# print(objEmployee.getName());

print(objEmployee.getEmpInfo())

print(objEmployee1.getEmpInfo())

# print(help(Employee))






