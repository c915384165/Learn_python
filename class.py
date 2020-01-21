class Person:
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname

  def print_name(self):
  	print(self.firstname, self.lastname)


p1 = Person("John", "Allan")
p1.print_name()

class Student(Person):
	def __init__(self, firstname, lastname, year):
		super().__init__(firstname, lastname)
		self.graduationyear = year

	def print_name(self):
		print(self.lastname, self.firstname)

p2 = Student("Allan", "Green", 2019)
p2.print_name()
print(p2.graduationyear)