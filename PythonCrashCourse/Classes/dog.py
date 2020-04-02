class Dog():
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name.title()} is now sitting')

    def roll_over(self):
        print(f'{self.name.title()} rolled over!')


my_dog = Dog('willie', 6)
print(f'My dog\'s name is {my_dog.name.title()}')
print(f'My dog is {my_dog.age} years old.')

my_dog.sit()
my_dog.roll_over()