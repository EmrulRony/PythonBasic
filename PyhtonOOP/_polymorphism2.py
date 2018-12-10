#---Method overloading---
# Method overloading concept is not same as JAVA or C++ in Python
# So we have to implement it in a different way

class Student:

    def sum(self,mark1=None,mark2=None,mark3=None):

        if (mark1!=None and mark2!=None and mark3!=None):
            sum=mark1+mark2+mark3
        elif (mark1!=None and mark2!=None):
            sum=mark1+mark2
        elif (mark1!=None):
            sum=mark1
        else:
            sum=0
        return sum;


obj = Student()

print(obj.sum())
