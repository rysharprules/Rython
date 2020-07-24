# Object Oriented Programming

- [Object Oriented Programming](#object-oriented-programming)
  - [Defining a class](#defining-a-class)
    - [Initialising an object](#initialising-an-object)
    - [Attributes](#attributes)
      - [Mutating class attributes](#mutating-class-attributes)
    - [Methods](#methods)
    - [`self`](#self)
    - [Dynamic object altering with `setattr`](#dynamic-object-altering-with-setattr)
    - [Decorators](#decorators)
      - [Add methods to classes with decorators](#add-methods-to-classes-with-decorators)
      - [`wraps`](#wraps)
      - [The `@property` decorator](#the-property-decorator)
        - [Encapsulation in Python](#encapsulation-in-python)
  - [Inheritance](#inheritance)
    - [Multiple inheritance](#multiple-inheritance)
    - [`super`](#super)
    - [Abstract classes](#abstract-classes)

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

### Initialising an object

To create a new object (_instance_) of `Bicycle` we assign a variable to `Bicycle` and set the default values (for `make` and `model`) via it's `__init__` method (constructor).

`my_bike = Bicycle("Cannondale", "Optimo")`

You can define a class without specifying an `__init__` method, in which case it will create an instance without any of its attributes set.

### Attributes

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

#### Mutating class attributes

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

### Methods

Methods describe the _behaviour_ of an object. Methods in an object take `self` as the first parameter. These functions are known as _instance methods_ because they are called on instances of the class. You omit the `self` argument when you call a method, Python takes care of passing the value of `self` for you:

`my_bike.change_gear(3)`

### `self`

`self` is the instance itself (synonymous with `this` in Java/C#). 

Our `Bicycle` method, `change_gear` defines the behaviour of changing gear for bicycles in general. Calling `my_bike.change_gear(3)` applies those
instructions to the `my_bike` instance which Python sends to the function for us via `self`.

Therefore, `my_bike.change_gear(3)` is just shorthand for `Bicycle.change_gear(my_bike, 3)` (which is perfectly valid (if rarely seen) code).

### Dynamic object altering with `setattr`

We can also add attributes and methods in a dynamic way, by using [setattr](https://pythonreference.readthedocs.io/en/latest/docs/functions/setattr.html). `setattr` assigns a value to the object’s attribute given its name:

`setattr (object, name, value)`

Where `object` is an object that allows its attributes to be changed. `name` is a string name of the attribute. `value` is a new value of any type for the attribute named in `name`.

For example, we have a `Tea` object:

````
class Tea(object):
  
  def __init__(self, type, ingredients): # constructor
    self.type = type
    self.ingredients = ingredients
  
  def prepare_tea(self): # use self.ingredients to make the tea
    (...)
````

Attributes can be an existing one or a newly created:

````
breakfast_tea = Tea("breakfast_tea", ["black_tea", ...])
setattr(breakfast_tea, "type", "blueberries tea")
setattr(breakfast_tea, "preparation_time", 20)
````

Methods can be changed too:

````
def prepare_sweet_tea(self): # add a lot of sugar & use self.ingredients to make the tea
  ...
setattr(breakfast_tea, "prepare_tea", prepare_sweet_tea) # only for the given object
setattr(Tea, "prepare_tea", prepare_sweet_tea) # for the class
````

However, "with great power comes great responsibility". So much freedom can end up with:
- Security vulnerabilities
- Bugs due to the change of class methods behavior or internal attributes in a way not expected by the class

### Decorators

[Decorators](https://book.pythontips.com/en/latest/decorators.html) can be added to functions.

It can be used to attach logic to a function, logging for example:

````
import datetime

def log_function_call(func):
  def with_logging(*args, **kwargs):
    func(*args, **kwargs)
    print(func.__name__ + " was called at " + datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
  return with_logging

@log_function_call
def say_hello():
  print("Hello")

say_hello()
````

`func` is an argument given to the function `log_function_call`. The expression `func()` means "call the function assigned to the variable `func`." The decorator is taking another function as an argument, and returning a new function (defined as `with_logging`) which executes the given function `func` when it is run.

To summarise, we have a function inside a function which returns that function. Using the `@` marks the function (`say_hello`) as requiring decoration.

We can get a function's name using `.__name__`. Using `func.__name__` gets the name of the function passed as `func`, in this case, `say_hello`.

See [Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/) for further reading.

#### Add methods to classes with decorators

You can go as far as adding methods to classes with decorators:

````
class A(object):
  def __init__(self):
    self.x = 0

  def add_method(cls):
    def decorator(func):
      setattr(cls, func.__name__, func)
      return func
    return decorator

@add_method(A)
def foo(self):
  print(self.x)

a = A()

a.foo() # should print 0 
````

Here we pass the class itself, `A` to the `add_method`, then use `setattr` to add the function `foo` to `A`.

#### `wraps`

If we call `print(say_hello.__name__)`, the output will be `wrapTheFunction`. Our function was replaced by `wrapTheFunction`. It overrode the name and docstring of our function. `functools.wraps` fixes this problem. Import:

`from functools import wraps`

Now we call with the added `@wraps` annotation in the decorator:

````
def log_function_call(func):
  @wraps(func)
  def with_logging(*args, **kwargs):
    func(*args, **kwargs)
    print(func.__name__ + " was called at " + datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
  return with_logging
````

`@wraps` takes a function to be decorated and adds the functionality of copying over the function name, docstring, arguments list, etc. This allows us to access the pre-decorated function’s properties in the decorator.

#### The `@property` decorator

Python has the OOP practice of getters and setters, which can be implemented with the `@property` decorator:

````
class Student(object):

  def __init__(self, name, age):
    self.name = name
    self.age = age

  @property
  def age(self):
    print("Get Value")
    return self._age

  @age.setter
  def age(self, value):
    print("Set Value")
    if value< 0:
      raise ValueError("Age below 0 is not possible")
    self._age = value

st = Student("Mark", 20) # set initial value with __init__
print(st.age) # get value (prints 20)
st.age = 25 # set value
print(st.age) # get value (prints 25)
````

Use `@decorator` for getters methods and `@{attribute}.setter` for the setter method.

##### Encapsulation in Python

See [Python — Encapsulation Does it exists??](https://medium.com/@manjuladube/encapsulation-abstraction-35999b0a3911).

## Inheritance

When creating a class, add the class in parentheses on the first line of
a class definition to specify the class that it inherits from:

`class Car(Vehicle):`

### Multiple inheritance

It is possible for a Python class to inherit from multiple base classes:

`class Car(Engine, Wheels):`

When inheriting from multiple base classes the base classes are often referred to as _mixins_ instead (as they are "mixedinto" the class). This can come in handy when you want to break down a class into multiple reusable components.

### `super`

The `super()` method, allows access to any of the base classes methods.

````
class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width

class Square(Rectangle):
  def __init__(self, length):
    super().__init__(length, length)
````

You can also use `super()` to access base methods from further down the inheritance hierarchy by providing the target class as a parameter:

````
class ColouredSquare(Square):
  def __init__(self, length, colour):
    self.colour = colour
    super(Rectangle).__init__(length, length) # Calls __init__ from Rectangle and not Square
````

### Abstract classes

Python's `abc` module contains a class named `ABC` (**abstract base class**). Making a class inherit from `ABC` and making one of its methods virtual will make that class an `ABC`. A virtual method is one that the `ABC` says must exist in child classes, but doesn't necessarily actually implement. Import `abc`:

`from abc import ABC, abstractmethod`

With `ABC` imported, a class can be marked as abstract by adding `ABC` to the class definition:

`class Vehicle(ABC):`

Now the class is abstract we can make abstract methods:

````
@abstractmethod
def vehicle_type(self):
````

Now, since `vehicle_type` has been marked as an abstract method, we can't directly create an instance of `Vehicle`:

````
vehicle = Vehicle() # Raises the following error
TypeError: Can't instantiate abstract class Vehicle with abstract methods vehicle_type
````