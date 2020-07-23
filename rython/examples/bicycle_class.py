class Bicycle:
    
    wheels = 2

    def __init__(self, make, model):
        self.make = make
        self.model = model
        # Start in first gear.
        self.gear = 1
    
    def change_gear(self, gear):
        self.gear = gear

my_bike = Bicycle("Cannondale", "Optimo")

print(my_bike.__class__) # <class '__main__.Bicycle'>
print(Bicycle.__class__)  # <class 'type'>
print(my_bike.__dict__)  # {'make': 'Cannondale', 'model': 'Optimo', 'gear': 1}
print(Bicycle.__dict__)
"""
{'__module__': '__main__', 'wheels': 2, '__init__': <function Bicycle.__init__ at 0x02E7D1D8>, 'change_gear': <function Bicycle.change_gear at 0x02E7D190>, '__dict__': <attribute '__dict__' of 'Bicycle' objects>, '__weakref__': <attribute '__weakref__' of 'Bicycle' objects>, '__doc__': None}
"""