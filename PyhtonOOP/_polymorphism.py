# This program demonstrate Polymorphism in Python
# Poly means many
# Morph means forms
# Four ways we can achive polymorphism in Python
# 1. Dock Typing
# 2. Operator overloading
# 3. Method overloading
# 4. Method overriding

#----Duck typing----

class Eclipse:

    def executes(self):
        print("Eclipse executes programs")

class Jetbeans:
    def executes(self):
        print("Executes progs")
        print("Spell checking")
        print("auto completion")
class Main:

    def code(self,obj):
        obj.executes()

# obj = Eclipse()
obj = Jetbeans()
mainObj = Main()
mainObj.code(obj)