class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'This is the {self.restaurant_name} serving {self.cuisine_type}')

    def open_restaurant(self):
        print(f'The restaurant is now open for everyone!')


gruby_benek = Restaurant('Gruby Benek', 'pizza')
gruby_benek.describe_restaurant()
gruby_benek.open_restaurant()

nel_parco = Restaurant('Nel Parco', 'pizza')
nel_parco.describe_restaurant()

mcdonald = Restaurant('Mc Donald\'s', 'Burgers')
mcdonald.describe_restaurant()
