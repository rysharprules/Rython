# Object Oriented Programming

- [Object Oriented Programming](#object-oriented-programming)
  - [Defining a class](#defining-a-class)
  - [Initialising an object](#initialising-an-object)
  - [Attributes](#attributes)
    - [Mutating class attributes](#mutating-class-attributes)
  - [Methods](#methods)
  - [`self`](#self)

## Defining a class

````
class Bicycle:
  
  wheels = 2
  
  def __init__(self, make, model):
    self.make = make
    self.model = model
    # Start in first gear.
    self.gear = 1;
  
  def change_gear(self, gear):
    self.gear = gear
````

A class is defined with the `class` keyword. Variables within a class are known as _class attributes_.

The `__init__` method sets the initial values for _instance attributes_: `make`, `model` and `gear`.

Within the class is a method definition named `change_gear` which changes the `gear` instance attribute value.

## Initialising an object

To create a new object (_instance_) of `Bicycle` we assign a variable to `Bicycle` and set the default values (for `make` and `model`) via it's `__init__` method (constructor).

`my_bike = Bicycle("Cannondale", "Optimo")`

You can define a class without specifying an `__init__` method, in which
case it will create an instance without any of its attributes set.

## Attributes

To access the value of an attribute on a specific object, you use _attribute reference syntax_: `obj.name` — where `obj` is the name of the object (e.g. `my_bike`) and `name` is the name of the attribute (e.g. `model`). For example:

````
print(my_bike.make) # Cannondale
print(my_bike.gear) # 1
print(my_bike.wheels) # 2
````

Similarly, you can assign values to object attributes using the same syntax:

````
my_bike.model = 'Topstone'
my_bike.gear = 2
print(my_bike.model) # Topstone
print(my_bike.gear) # 2
````

Note that instance and class attributes are accessed in the same way; however, class attributes can also be accessed directly from the class, whereas instance attributes can't (because they are only defined for a given instance) - similar to `static` variables in Java albeit with some caveats discussed next:

````
print(Bicycle.wheels) # 2
print(Bicycle.make) # AttributeError: type object 'Bicycle' has no attribute 'make'
````

### Mutating class attributes

Class attributes are mutatable, but they _should_ be kept constant to keep code cleaner and easier to understand, and to avoid surprising behaviour and tricky bugs.

For example:

````
class MyClass:
  mutableClassVariable = ['Hello']

obj1 = MyClass()
obj2 = MyClass()
````

When re-assigning the class variable on the class object, we update the value for everyone/all instances. This is because all instances reference the same class object, so if we change that, we affect everything:

````
MyClass.mutableClassVariable.append('World')
print(obj1.mutableClassVariable) # ['Hello', 'World']
print(obj2.mutableClassVariable) # ['Hello', 'World']
print(MyObject.mutableClassVariable) # ['Hello', 'World']
````

When re-assigning the class variable via the instance, what actually happens is that python sets a new instance attribute with the same name. This new attribute hides the original one:

````
obj1.mutableClassVariable = ['Hello', 'World']
print(obj1.mutableClassVariable) # ['Hello', 'World']
print(obj2.mutableClassVariable) # ['Hello']
print(MyClass.mutableClassVariable) # ['Hello']
````

When mutating the class variable, all the references are untouched - so when we change the value that everything refers to, we effectively update all the variables.

````
obj1.mutableClassVariable.append('World')
print(obj1.mutableClassVariable) # ['Hello', 'World']
print(obj2.mutableClassVariable) # ['Hello', 'World']
print(MyClass.mutableClassVariable) # ['Hello', ‘World']
````

## Methods

Methods describe the _behaviour_ of an object. Methods in an object take `self` as the first parameter. These functions are known as _instance methods_ because they are called on instances of the class. You omit the `self` argument when you call a method, Python takes care of passing the value of `self` for you:

`my_bike.change_gear(3)`

## `self`

`self` is the instance itself (synonymous with `this` in Java/C#). 

Our `Bicycle` method, `change_gear` defines the behaviour of changing gear for bicycles in general. Calling `my_bike.change_gear(3)` applies those
instructions to the `my_bike` instance which Python sends to the function for us via `self`.

Therefore, `my_bike.change_gear(3)` is just shorthand for `Bicycle.change_gear(my_bike, 3)` (which is perfectly valid (if rarely seen) code).