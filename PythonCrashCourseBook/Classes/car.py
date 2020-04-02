class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return formated name for the car"""
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back an odometer')

    def increment_odometer(self, mileage):
        self.odometer_reading += mileage

    def read_odometer(self):
        """Print the statement showing the car's mileage"""
        print(f'This car has {self.odometer_reading} miles on it')


# my_car = Car('audi', 'a4', 2016)
# my_car.update_odometer(25)
# print(my_car.get_descriptive_name())
# my_car.increment_odometer(10000)
# my_car.read_odometer()