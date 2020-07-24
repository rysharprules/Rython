class Vehicle:
    
    base_sale_price = 0

    def __init__(self, wheels, make, model, miles):
        self.wheels = wheels
        self.make = make
        self.model = model
        self.miles = miles

    def sale_price(self):
        return 5000.0 * self.wheels

    def purchase_price(self):
        return self.base_sale_price - (0.1 * self.miles)


class Car(Vehicle):
    def __init__(self, wheels, make, model, miles):
        self.base_sale_price = 8000
        self.wheels = wheels
        self.make = make
        self.model = model


class Truck(Vehicle):
    def __init__(self, wheels, make, model, miles):
        self.base_sale_price = 10000
        self.wheels = wheels
        self.make = make
        self.model = model
        self.miles = miles