# This program demonstrate Method overriding

class A:
    def show(self):
        print("in A show")

class B(A):
    def show(self):
        print("in B show")

obj=B()
obj.show()