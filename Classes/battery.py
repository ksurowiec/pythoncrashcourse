class Battery():
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'This car has a {self.battery_size}-kWh battery')

    def get_range(self):
        if self.battery_size == 70:
            distance = 240
        elif self.battery_size == 85:
            distance = 270
        else:
            distance = '?'

        print(f'With the current battery capacity your car can travel up to {distance} miles.')