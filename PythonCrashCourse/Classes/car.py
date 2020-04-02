class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return formated name for the car"""
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()


my_car = Car('audi', 'a4', 2016)
print(my_car.get_descriptive_name())