class Person:

    def __init__(self, firstname, surname, age):
        self.firstname = firstname
        self.lastname = surname
        self.age = age


def talk(self):
        talk = self.firstname
        print(self.firstname)
        talk = self.lastname
        print(self.lastname)
        talk = self.age
        print(self.age)

person1 = Person('Carl', 'Johnson', '26')
print('Hello, my name is', person1.firstname + ' ' + person1.lastname, 'and I’m', person1.age, 'years old')
