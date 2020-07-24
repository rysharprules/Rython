from abc import ABC, abstractmethod


class Vehicle(ABC):
    
    base_sale_price = 0
    wheels = 0

    def __init__(self, make, model, miles):
        self.make = make
        self.model = model
        self.miles = miles

    def sale_price(self):
        return 5000.0 * self.wheels
    
    def purchase_price(self):
        return self.base_sale_price - (0.1 * self.miles)

    @abstractmethod
    def vehicle_type(self):
        pass


class Car(Vehicle):

    base_sale_price = 8000
    wheels = 4

    def vehicle_type(self):
        return 'car'

class Truck(Vehicle):

    base_sale_price = 10000
    wheels = 4

    def vehicle_type(self):
        return 'truck'


class Motorcycle(Vehicle):

    base_sale_price = 4000
    wheels = 2

    def vehicle_type(self):
        return 'motorcycle'
