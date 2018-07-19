
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cannot roll back the odometer')

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print('Your gas tank has been filled')


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + ' Kwh battery')

    def fill_gas_tank(self):
        print("You have an electric car so you don't need gas.")


class Battery:
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This battery has size of " + str(self.battery_size))


new_gas_car = Car('Infiniti','G37', '2013')
print(new_gas_car.get_descriptive_name())
new_gas_car.fill_gas_tank()

new_electric_car = ElectricCar('Tesla', 'Model S', '2016')
print(new_electric_car.get_descriptive_name())
new_electric_car.fill_gas_tank()

