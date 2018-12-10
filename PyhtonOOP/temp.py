class A():
	# i=4
	# j=5
	def __init__(self):
		self.i=1
		self.j=2
	def metA(self):
		print("In class A met")


class B(A):
	def __init__(self):
		A.__init__(self)
		self.x = 1
		self.y = 2

	def metA(self):
		print("In class B met")

	def margeMets(self):
		z = self.i + self.j
		print(z)

b = B()
b.metA()
b.margeMets()

