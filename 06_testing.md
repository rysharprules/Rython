# Testing

**Pages**
| Previous | Home | Next |
|---|---|---|
| [Oauth](https://github.com/rysharprules/Rython/blob/master/05_oauth.md) | [Home](https://github.com/rysharprules/Rython) | |

----

**Contents**
- [Testing](#testing)
  - [](#)

## Static analysis tools

A few common Python static analysis tools are listed below to give you a flavour of the variety out there. This is by no means an exhaustive list!

- [Black](https://pypi.org/project/black/): code reformatter
- [Pyflakes](https://pypi.org/project/pyflakes/): quick checking for common runtime errors
- [Flake8](https://pypi.org/project/flake8/): a wrapper around pyflakes, plus enforcement of the (somewhat outdated) PEP 8 conventions
- [Mypy](https://pypi.org/project/mypy/): enforces type annotations
- [Pylint](https://pypi.org/project/pylint/): assorted linting options (error detection, code style)

## Unit testing

### Structure

Code inside a test method has three parts:

1. The test setup, where we specify the input to the function
1. A call to the function we're testing
1. An assertion that the function returned the value we expect 
 
This structure is sometimes called _Arrange/Act/Assert_ or _Given/When/Then_.

### Tools

#### Unittest

Unittest is the testing framework included in the Python standard library.

````
from unittest import TestCase

class TestStringMethods(TestCase):
  
  def test_upper(self):
    self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
    self.assertTrue('FOO'.isupper())
    self.assertFalse('Foo'.isupper())

  def test_split(self):
    s = 'hello world'
    self.assertEqual(s.split(), ['hello', 'world']) 
    with self.assertRaises(TypeError): # check that s.split fails when the separator is not a string
      s.split(2)
````

Unittest can then be launched by the following from Python:

````
import unittest
unittest.main()
````

#### Pytest

[Pytest](https://docs.pytest.org/en/stable/) is a widely used testing framework for the Python language. We'll be using Pytest for the remainder of this section and examples.

You can install pytest via `pip` or another package manager, for example:

`pip install pytest`

To run pytest, simply run the following command from the root of your project:

`pytest`

Here's how it works:

1. You write test functions that include assertions.
2. You run pytest.
3. Pytest automatically discovers your test functions, runs them, and reports any failed assertions.

````
import pytest

def test_upper():
  assert 'foo'.upper() == 'FOO'

def test_isupper():
  assert 'FOO'.isupper()
  assert not 'Foo'.isupper()

def test_split():
  s = 'hello world'
  assert s.split() == ['hello', 'world'] # check that s.split fails when the separator is not a string
  with pytest.raises(TypeError):
    s.split(2)
````

Pytest discovers tests by a few default rules:

- Test function or method names must be prefixed with "test".
- If used, test class names must be prefixed with "Test".
- Tests must live in files named test_*.py or *_test.py

It's common to use a test package structure that mirrors the package structure in source code, but this is not required. There are many other ways to structure your tests, and you can read recommendations and tips on the [pytest documentation](https://docs.pytest.org/en/stable/goodpractices.html#test-package-name).

### Fixtures

````
def test_car_moves():
  car = Car()
  car.add_driver()
  car.start()
...

def test_car_stops():
  car = Car()
  car.add_driver()
  car.start()
...
````

In some testing frameworks these are called _"SetUp"_ and _"TearDown"_ methods. Pytest approaches the problem slightly differently, with elegant solutions known as **"fixtures"**. The code above can be re-written to use a fixture:

````
import pytest

@pytest.fixture
def moving_car():
  car = Car()
  car.add_driver()
  car.start()
  return car

def test_car_moves(moving_car):
  ...

def test_car_stops(moving_car):
  ...
````

The fixture is called once per test, so each test gets a separate `Car` object. Tests can then focus to test-specific details (the "Act" and "Assert" parts), while sharing the common setup logic.

Fixtures can also contain teardown code:

````
@pytest.fixture
def http_connection():
  http_connection = http.client.HTTPConnection('www.python.org')
  yield http_connection # provide the fixture value
  print("teardown http client")
  http_connection.close()
````

All code after `yield` is executed after the test, and can contain teardown instructions.

You can share fixtures between multiple test files by defining them in a `conftest.py` file.

### Handling Errors

Use the `pytest.raises()` context manager:

````
def test_cant_add_number_to_string():
  text = 'a'
  number = 3
  with pytest.raises(TypeError):
    text + number
````

The test above will only succeed if line 5 throws a TypeError (or subclass). If the code runs successfully, or an exception is raised elsewhere, or the exception is not a TypeError, the test will fail.

You can catch any error with `Exception`, although this is bad practice.

### Parametrised Tests

Pytest provides **parametrised test** functionality through a built-in decorator. The example below shows a test that will be run four times, with the
parameters `0`, `1`, `"hello"` and `"world"` in turn.

````
@pytest.mark.parametrize("value", [0, 1, "hello", "world"])
def test_process_value(value):
  ...
````

If you want to parameterise multiple parameters in a unit test you can use tuple syntax (similar to how you can return multiple values from a function):

````
import pytest
@pytest.mark.parametrize("test_input, expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
  assert eval(test_input) == expected
````

When dealing with a large number of test parameters it's often cleaner to assign the test parameter collection to a variable beforehand:

````
import pytest

test_params = [("3+5", 8), ("2+4", 6), ("6*9", 42)]

@pytest.mark.parametrize("test_input, expected", test_params)
def test_eval(test_input, expected):
  assert eval(test_input) == expected
````

This also allows for the params to be shared between tests.

## Code Coverage

Pytest has a plugin, [pytest-cov](https://pypi.org/project/pytest-cov/), that provides code coverage reports for python projects. Once installed, you can optionally include coverage reporting when you invoke pytest by running:

`pytest --cov=<PATH_TO_PACKAGE>`

Alternatively, to always generate coverage data when running pytest you can add a `pytest.ini` file in your project root and specify the coverage option there:

````
[pytest]
addopts = —cov=<PATH_TO_PACKAGE>
````

## Test doubles and mocking strategies

A **test double** is an object used in place of a real object for testing purposes. "Test double" is a broad term that encompasses a few different strategies and goals. In all cases, the purpose of a test double is to limit the scope of a test to the system/class/function you're interested in. The particular kind of test double used will depend on what you need to achieve to satisfy the test logic. There are three main types:

- A **Stub** object has no logic, and returns preprogrammed values to calls on its methods.
- A **Spy** object records details about how it was used (e.g. what methods were called, how many times, and with what parameters).
- A **Fake** object is more sophisticated than a stub. It has real functionality, but take some shortcuts to facilitate testing. A good example would be using a in-memory database, or dropping a slow validation step used in production code.

### Python tools

Firstly, [unittest.mock](https://docs.python.org/3/library/unittest.mock.html) is bundled in the standard library. Despite its name (a subpackage
of unittest), it is not tightly coupled to the unittest framework and can be used easily with other testing frameworks (e.g. pytest).

Secondly, pytest provides some mocking functionality through its [monkeypatch](https://docs.pytest.org/en/latest/monkeypatch.html) fixture. You don't need to configure anything extra to use this, simply add the 'monkeypatch' argument to a test and pytest will inject the fixture.

#### Example

````
from random import random
from typing import Iterable

class Sheep:
  
  def __init__(self, weight: float):
    self._weight = weight

  def get_wool(self):
    return random() * self._weight

class Shears:
  
  def __init__(self, efficiency: float):
    self._efficiency = efficiency

  def shear(self, targets: Iterable[Sheep]):
    wool = 0
    print('Sharpening shears...')
    for target in targets:
      print(f'Shearing a {target.__class__.__name__}')
      wool += target.get_wool()
    return wool * self._efficiency
````

Below is an example of using these classes together, and some example output:

````
flock = (
  Sheep(10),
  Sheep(4.3),
  Sheep(2)
)
shears = Shears(0.8)
wool = shears.shear(flock)

> Sharpening shears...
> Shearing a Sheep
> Shearing a Sheep
> Shearing a Sheep
> Wool: 7.133562646044543
````

Using monkeypatch, we can quickly stub the functionality of the `Sheep` class:

````
def test_shears(monkeypatch):
  """ Arrange """
  wool_per_sheep = 1
  efficiency = 0.5
  monkeypatch.setattr(Sheep, 'get_wool', lambda self: wool_per_sheep)
  flock = (
    Sheep(5.4), # weight is irrelevant
    Sheep(2.1)
  )
  shears = Shears(efficiency)

  """ Act """
  wool = shears.shear(flock)
  
  """ Assert """
  assert wool == len(flock) * wool_per_sheep * efficiency
````

## Integration testing

**werkzeug** (the framework Flask is built on) provides a development web client that is extremely helpful for integration testing:

````
import pytest
from myapp import app

@pytest.fixture
def test_client():
  """This fixture provides a flask test client"""
  with app.test_client() as client:
    yield client

def test_get_root(test_client):
  """Check a GET request to root path works"""
  response = test_client.get('/')
  assert response.status_code == 200
  """ additional response checks go here """
````

## End-to-end testing

[Selenium](https://www.selenium.dev/) is a popular open-source UI testing library. To get set up, you'll need to download a web driver for a browser you have installed locally. You can find webdrivers on listed on the [selenium docs](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/). For example, if you're using Google Chrome you can download an appropriate driver directly from [Google](https://chromedriver.storage.googleapis.com/index.html). 

The test script below will programmatically load a website in Chrome and test the title is as expected:

````
import pytest
from selenium import webdriver

""" Module scope re-uses the fixture """
@pytest.fixture(scope='module')
def driver():
  """ path to your webdriver download """
  with webdriver.Chrome('./chromedriver') as driver:
    yield driver

def test_python_home(driver):
  driver.get("https://www.python.org")
  assert driver.title == 'Welcome to Python.org'

def test_downloads_page(driver):
  driver.get("https://www.python.org")
  link = driver.find_element_by_link_text('Downloads')
  link.click()
  assert driver.current_url == 'https://www.python.org/downloads/'
````

### Headless browsers

To run Selenium with Google Chrome in headless mode, you can modify the fixture shown earlier to add the appropriate configuration option:

````
@pytest.fixture(scope='module')
def driver():
  """ path to your webdriver download """
  opts = webdriver.ChromeOptions()
  opts.add_argument('--headless')
  with webdriver.Chrome('./chromedriver', options=opts) as driver:
    yield driver
````

## Snapshot testing

A snapshot tool compares your test output with previous outputs, and warns you if it has detected any change. You don't need to provide an
expected result - it generates one for you the first time you run the test.

Below are just a few tools in this space:

- [snapshottest](https://pypi.org/project/snapshottest/) - a python package for snapshot testing
- [Jest Snapshot testing](https://jestjs.io/docs/en/snapshot-testing) - a common option in the Javascript ecosystem, primarily for testing web interfaces
- [BackstopJS](https://github.com/garris/BackstopJS) - snapshot testing web interfaces using screenshots!

## Contract testing

You tell a testing tool what you expect the interactions between two services to look like (the contract), and it verifies that both services adhere to the contract. A popular option is [Pact](https://docs.pact.io/faq/convinceme).

## Laboratory/Scientist

[Laboratory](https://github.com/joealcorn/laboratory) is a library for Python that is inspired by GitHub's [Scientist](https://github.com/github/scientist) library for Ruby. Put simply, it allows you to run an alternative codepath alongside the original, unrefactored code, while testing for changes in return values or regressions in performance. This technique can be used in combination with **Branching by Abstraction** to safely test moving over methods/endpoints from the abstraction to the new service before committing to the move. This [GitHub blog post](https://github.blog/2016-02-03-scientist/) goes into more detail on how these tools should be used.