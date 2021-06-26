
class Animal:
	def hello(self):
		print('Hello, choice your animal')

	def talk(self):
		print('You have two option\n')

class Dog(Animal):
	def talk(self):
		print ('Dog say woof woof')

class Cat(Animal):
	def talk(self):
		print('Cat say meow')


say_animal = Animal()
say_dog = Dog()
say_cat = Cat()


say_animal.hello()
say_animal.talk()

say_dog.hello()
say_dog.talk()

say_cat.hello()
say_cat.talk()

