# Fundamentals

- [Fundamentals](#fundamentals)
  - [Installation](#installation)
  - [Basics](#basics)
    - [REPL](#repl)
    - [Comments](#comments)
  - [Data Types and Variables](#data-types-and-variables)
    - [Variable Name Restrictions](#variable-name-restrictions)
      - [Keywords](#keywords)
      - [Naming](#naming)
    - [Variable Creation](#variable-creation)
  - [Common Data Types](#common-data-types)
    - [String](#string)
      - [Concatenation](#concatenation)
      - [Length](#length)
      - [Case (upper and lower)](#case-upper-and-lower)
      - [Character access](#character-access)
      - [Slices](#slices)
    - [Numbers](#numbers)
      - [Casting](#casting)
    - [Boolean](#boolean)
      - [Combining Boolean expressions](#combining-boolean-expressions)
        - [Precedence](#precedence)
  - [Complex Data Types](#complex-data-types)
    - [Array](#array)
    - [List](#list)
      - [Accessing a list item](#accessing-a-list-item)
      - [Modify a list](#modify-a-list)
      - [Accessing sublists](#accessing-sublists)
      - [Removing items from a list](#removing-items-from-a-list)
      - [Adding items to a list](#adding-items-to-a-list)
      - [Concatenation](#concatenation-1)
      - [Length](#length-1)
      - [Copy](#copy)
    - [Dictionary](#dictionary)
      - [Accessing individual items](#accessing-individual-items)
      - [Adding to and modifying](#adding-to-and-modifying)
      - [Removing items](#removing-items)
      - [Length](#length-2)
    - [Set](#set)
  - [Flow Control](#flow-control)
    - [Condtions](#condtions)
    - [Code Blocks](#code-blocks)
  - [Flow Control Statements](#flow-control-statements)
    - [If Statements](#if-statements)
    - [Else Statements](#else-statements)
    - [Elif Statements](#elif-statements)
    - [While loops](#while-loops)
      - [Break and Continue Statements](#break-and-continue-statements)
    - [For Loops](#for-loops)
      - [`range` function](#range-function)
      - [`enumerate` function](#enumerate-function)
      - [List Comprehension](#list-comprehension)
    - [Try, Except and Finally](#try-except-and-finally)
      - [Error Types](#error-types)
  - [Functions](#functions)
    - [Returning data](#returning-data)
  - [Note To Read Later](#note-to-read-later)

## Installation

You can download the latest version of Python from [here](https://www.python.org/downloads/). 

_Note: Version **3.8.3** was used in this course._

## Basics

Check the [Python documentation](https://docs.python.org/3/) to clarify how a given feature works.

### REPL 

Python has a REPL (Read-eval-print loop”) environment. This is accessed on the command line with:

````
C:\Users\Ryan>python -i
Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 1 + 2
3
````

### Comments

There are two types of comments:

- Single line which can also be done after a line of code with hash: `# a comment`
- Multi line comment with three double quotes:
  - ````
    """
    multiline comment
    """
    ````

## Data Types and Variables

All variables in Python are what are known as references. This means that when you
assign a variable to a value, that variable is an `alias` for that value. For complex data types like lists this can mean that changing the values for one variable may result in changes for another as they point to the same object reference.

### Variable Name Restrictions

#### Keywords

Python has a set of reserved keywords, which are listed below using `keyword.kwlist`.

````
>>> import keyword
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>>
````

#### Naming

Variable names must:

1. Start with a letter or underscore
1. Be composed purely of alphanumeric characters (letters and numbers) or underscores

### Variable Creation

You can create a variable simply by assigning it. Python will infer the type.

````
>>> my_name = 'John Smith'
>>> my_age = 42
````

When using the Python REPL, you can see what value is held by a variable by simply typing the name of the variable into the interactive shell. Python will evaluate the expression you have typed, which in this case
simply means getting the value of the variable.

````
>>> my_age
42
````

## Common Data Types

### String

Strings are surrounded by single or double quotes - see [this description of quote usage](https://stackoverflow.com/questions/56011/single-quotes-vs-double-quotes-in-python).

See [Python's documentation for further string operations.](https://docs.python.org/3/library/stdtypes.html#string-methods)

Python strings are **immutable**, meaning that they can't be changed once they have been
created. Instead, if we want to alter a string we need to build a modified copy of the original:

`my_string = 'd' + my_string[1:]`

Immutability allows useful assumptions and optimisations, particularly for parallelisation.

#### Concatenation

With literals:

`>>> 'apples ' + 'bananas'` results in `'apples bananas'`

With variables:

````
>>> first_string = 'Hello'
>>> second_string = 'World'
>>> first_string + second_string # 'HelloWorld'
````

Multiple copies of a string can be joined with the multiplication operator:

````
>>> na = 'Na'
>>> batman = 'Batman!'
>>> 8 * na # 'NaNaNaNaNaNaNaNa'
>>> 8 * na + ' ' + batman # 'NaNaNaNaNaNaNaNa Batman!'
````

**Python is a strongly typed language**, so it will raise a `TypeError` if you tried to concat literal numbers to a string or use numeral operators such the minus (`-`) or divisor (`/`) on a string. The below will all fail with an error:

````
`>>> 'apples' + 7`
Traceback (most recent call
last): File "<stdin>", line
1, in <module>
TypeError: can only
concatenate str (not "int")
to str
````

You would need to explicitly cast the number to a string using the `str` function before it can be added:

````
>>> 'Total = ' + str(18)
'Total = 18'
````

#### Length

`>>> len('coconuts')` returns the length of the string, i.e. `8`

#### Case (upper and lower)

`>>> 'DrAGoNfRuiT'.lower()` returns the lower case version of this string, `'dragonfruit'`.

`>>> 'eLDeRbeRrY'.upper()` returns the upper case version of this string, `'ELDERBERRY'`.

#### Character access

Access individual characters using square brackets. Python indexes from 0. You can use a negative index to get characters from the back of the string instead of the front. The index -1 is the first character from the back, and so on.

````
>>> a_string = 'Example'
>>> a_string[0] # E
>>> a_string[1] # x
>>> a_string[6] # e
>>> a_string[-1] # e
>>> a_string[-3] # p
````

You cannot reassign characters:

````
>>> a_string[0] = 'F'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
````

#### Slices

You can obtain a string consisting of the part of a string between a start point and an end point – this is  called a _slice_ of the original string. The character at the start index is included in the slice, and the character at the end index is not included. You should think of the slice as stopping just before that character.

If you leave out either the start (or the end) index, then Python assumes that you want to start from the beginning of the string (or go all the way to the end).

````
>>> original_string = 'Supercalifragilistic'
>>> original_string[0:5] # 'Super'
>>> original_string[5:9] # 'cali'
>>> original_string[:5] # 'Super'
>>> original_string[9:] # 'fragilistic'
````

### Numbers

You can use both whole numbers (_integers_) and decimal numbers (_floating points_):

````
>>> an_integer_value = 7
>>> a_negative_value = -13
>>> a_floating_point_value = 1.34
````

You can use all the mathematical operations that you're used to:

````
>>> six = 2 + 4
>>> four = 6 - 2
>>> twelve = 2 * 6
>>> eight = 16 / 2
>>> twenty_seven = 3 ** 3
>>> ten = 2 * (1 + 4)
````

_Note: `**`, is the Python version of the exponentiation operator, which you might know as the “power
of” operator: above it calculates 3 to the power of 3._

#### Casting

You can cast to an int with the `int()` function.

### Boolean

Booleans are written with capital letters: `True` and `False`. _Equality_ (`==` and `!=`) and _comparison operators_ (`>`, `>=`, `<`, `<=`) result in Boolean values:

````
>>> 2 + 3 == 5 # True
>>> 2 + 3 != 5 # False
>>> 1 + 2 < 3 # False
>>> 1 + 2 <= 3 # True
>>> 2 + 3 > 5 # False
>>> 2 + 3 >= 5 # True
>>> "apple" < "banana" # True, using alphabetical order
>>> "coconut" == "coco" + "nut" # True
````

#### Combining Boolean expressions

• `not` x is True if y is False and vice-versa
• x `and` y is True only when both x and y are True
• x `or` y is True if either one of x and y are True, or if both of them are True

##### Precedence

The use of parentheses (brackets) is entirely optional, but makes it clear what order various numerical and Boolean operators are working in - otherwise precedence comes into play.

The complete list of operators grouped by precedence can be found [here](https://docs.python.org/3/reference/expressions.html#operator-precedence).

## Complex Data Types

### Array

You must fix the type of value that can be inserted into an `array`. That type is restricted to numerical types and single characters. The interpreter doesn't need to check the type of each item in an array, unlike with a list, leading to a performance improvement.

### List

Lists are useful when we want to store a sequence of data in a particular order.

Valid lists:

````
>>> list_of_numbers = [1, 2, 3, 4, 5]
>>> list_of_strings = ['one', 'two', 'three', 'four', 'five']
>>> list_of_booleans = [False, True, True, False, True]
>>> mixed_list = [1, 'two', 'three', 4, 'five']
>>> empty_list = []
````

#### Accessing a list item

Values are accessed with sqaured brackets:

````
>>> list_of_animals = ['armadillo', 'bear', 'crocodile', 'deer', 'elephant']
>>> list_of_animals[0] # 'armadillo'
>>> list_of_animals[1] # 'bear'
>>> list_of_animals[4] # 'elephant'
>>> list_of_animals[-1] # 'elephant'
>>> list_of_animals[-3] # 'crocodile'
````

#### Modify a list

````
>>> my_list = [1, 2, 3]
>>> my_list[0] = 4
>>> my_list # [4, 2, 3]
````

#### Accessing sublists

Sublists are accessed similar to string slices where the item at the starting index is included, the item at the ending index is not included.

````
>>> my_list = ['These', 'are', 'some', 'words', 'in', 'a', 'list']
>>> my_list[0:3] # ['These', 'are', 'some']
>>> my_list[4:5] # ['words']
>>> my_list[:3] # ['These', 'are', 'some']
>>> my_list[4:] # ['in', 'a', 'list']
````

#### Removing items from a list

You can remove items or slices of a list with the `del` statement:

````
>>> list_one = [1, 2, 3, 4, 5]
>>> del list_one[1]
>>> list_one # [1, 3, 4, 5]

>>> list_two = [1, 2, 3, 4, 5]
>>> del list_two[1:3]
>>> list_two # [1, 4, 5]
````

If you know which value you want to remove from the list, but not which index it is at, you can instead use the `remove` method. If the item appears more than once, only the first instance is removed.

````
>>> list_of_numbers = [3, 1, 4, 5, 7, 2, 6]
>>> list_of_numbers.remove(4)
>>> list_of_numbers # [3, 1, 5, 7, 2, 6]

>>> list_with_repeats = [1, 2, 1, 3, 2]
>>> list_with_repeats.remove(2)
>>> list_with_repeats # [1, 1, 3, 2]
>>> list_with_repeats.remove(1)
>>> list_with_repeats # [1, 3, 2]
````

#### Adding items to a list

You can add an item onto the end of a list using the `append` method:

````
>>> my_list = [1, 2, 3]
>>> my_list.append(4)
>>> my_list # [1, 2, 3, 4]
````

You can add an item somewhere in the middle of the list using the `insert` method, where the first argument is the insertion position and the second is the value:

````
>>> my_list.insert(1, 5)
>>> my_list # [1, 5, 2, 3, 4]
````

#### Concatenation

You can join together two lists to make a longer list using the addition (`+`) operator:

````
>>> first_list = [1, 2, 3]
>>> second_list = [4, 5, 6]
>>> first_list + second_list # [1, 2, 3, 4, 5, 6]
````

You can join together multiple copies of a list with itself using the multiplication (`*`) operator:

````
>>> other_list = [1, 2, 3]
>>> other_list * 3 # [1, 2, 3, 1, 2, 3, 1, 2, 3]
````

#### Length

You can get the length of a list using the `len` function:

````
>>> my_list = [1, 2, 3, 4]
>>> len(my_list) # 4
````

#### Copy

To get a copy of a list:

````
a_variable = [1, 2]
another_variable = a_variable.copy()
````

This avoids multiple variables pointing to the same reference list.

### Dictionary

This data type stores _key-value_ pairs similar to a `Map` in Java, where each key is unique.

Unlike lists, dictionaries are unordered. 

````
>>> dictionary_of_favourite_colours = {'Alice': 'Purple', 'Bob': 'Green', 'Charlie': 'Scarlet'}
>>> empty_dictionary = {}
````

#### Accessing individual items

Use the key to access the item value:

````
>>> dictionary_of_favourite_colours = {'Alice': 'Purple', 'Bob': 'Green', 'Charlie': 'Scarlet'}
>>> dictionary_of_favourite_colours['Alice'] # 'Purple'
>>> dictionary_of_favourite_colours['Bob'] # 'Green'
>>> dictionary_of_favourite_colours['Charlie'] # 'Scarlet'
````

#### Adding to and modifying

````
>>> favourite_colours = {}
>>> favourite_colours['Alice'] = 'Purple'
>>> favourite_colours['Bob'] = 'Green'
>>> favourite_colours # {'Alice': 'Purple', 'Bob': 'Green'}
````

If you try to add a value to a key that already exists, then it will simply be overwritten with the new value:

````
>>> favourite_colours = {}
>>> favourite_colours['Alice'] = 'Yellow'
>>> favourite_colours['Alice'] = 'Purple'
>>> favourite_colours # {'Alice': 'Purple'}
````

#### Removing items

You can remove an item from a dictionary with its key and the `del` statement:

````
>>> favourite_colours = {'Alice': 'Purple', 'Bob': 'Green', 'Charlie': 'Scarlet'}
>>> del favourite_colours['Bob']
>>> favourite_colours # {'Alice': 'Purple', 'Charlie': 'Scarlet'}
````

_Note: `KeyError` will be thrown if the key is missing when using `del`._

#### Length

You can get the length of a dictionary using the `len` function:

````
>>> favourite_colours = {'Alice': 'Purple', 'Bob': 'Green', 'Charlie': 'Scarlet'}
>>> len(favourite_colours) # 3
````

### Set

A set is essentially a dictionary but without values. Set's are similar to lists except they do not allow duplicates and looking up an item by key in a set is relatively fast compared to looking up an item by value in a list.

````
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)
{'orange', 'banana', 'pear', 'apple'} # duplicates have been removed
>>> 'orange' in basket True
>>> 'crabgrass' in basket False
````

## Flow Control

There are several types of flow control statement. Most of them consist of two important parts:

1. a condition
1. code blocks

### Condtions

A _condition_ in Python is any Boolean expression, i.e. anything that evaluates to `True` or `False`.

### Code Blocks

Lines of code are grouped together in blocks using _indentation_. Lines with the same level of indentation belong to the same block, and you start a new code block within the current block by increasing the indentation level. When you want to return to the outer code block, simply return the indentation level to match the outer block. It's conventional for programs to begin with no indentation, and for each nested code block to have **four** more spaces of
indentation than its parent block.

## Flow Control Statements

### If Statements

`if` statements consist of the following:

- The `if` keyword
- An expression
- A colon
- A code block, starting on the line after the expression

````
if True:
  print('First if statement')

if False:
  print('Second if statement')

if 1 + 2 == 3:
  print('Third if statement')

if 1 > 2 or 3 < 4:
  print('Fourth if statement')
````

Answers by statement:

1. This is printed.
1. This is not printed.
1. 1 + 2 == 3 evaluates to True so this is printed.
1. 3 < 4 is true so this is printed.

### Else Statements

The code block of an `if` statement can, optionally, be followed by an `else` statement. The `else` acts as a counterpart to the `if` — it will be executed exactly when the `if` statement's condition is `False`. An `else` statement doesn't have its own condition, because it relies entirely on the resolution of the `if` condition.

An `else` statement simply consists of the keyword `else` and a colon, and then a code block starting on the next line.

````
if True:
  print('First if statement')
else:
  print('First else statement')

if False:
  print('Second if statement')
else:
  print('Second else statement')

if 1 + 2 == 3:
  print('Third if statement')
else:
  print('Third else statement')

if 1 > 2 or 3 < 4:
  print('Fourth if statement')
else:
  print('Fourth else statement')
````

Answers by if/else statement:

1. First if statement.
1. Second else statement.
1. Third if statement.
1. Fourth if statement.

### Elif Statements

Similar to an `else` it can only follow an `if` statement. It can also follow another `elif` statement. `elif` statements include an additional condition, similar to `else if` in other languages.

````
if age < 2:
  print('You are a baby')
elif age < 18:
  print('You are a child')
elif age < 100:
  print('You are an adult')
else:
  print('You are really old!')
````

### While loops

The `if` statement checks its condition only once, and executes the code block once `if` the condition is `True`. On the other hand, the `while` statement checks its condition multiple times — once at the start, and once after each execution of the code block — and for as long
as the condition continues to be `True`.

A `while` statement consists of:

- The `while` keyword
- A condition
- A colon
- A code block beginning on the next line

````
times_run = 0
while times_run < 10:
  print('Hello!')
  times_run = times_run + 1
````

````
password = ''
while password != 'secret':
  password = input('What is the password?')
print('Access granted')
````

#### Break and Continue Statements

The `break` keyword exits the loops, even if the condition is still `True`. The `continue` keyword exits the _current_ iteration of the loop, going back to tthe condition check on the `while`.

````
while True:
  password = input('What is the password?')
  if password == 'secret':
    break
print('Access granted')

while True:
  username = input('What is your username?')
  if username != 'admin':
    continue
  password = input('What is the password?')
  if password == 'topsecret':
    break
print('Access granted')
````

### For Loops

Whereas the while loop keeps looping for as long as its condition is `True`, a for loop is for running some code a certain number of times.

A for loop consists of the following parts:
- The for keyword
- A variable name (it doesn't need to exist yet) for the _loop variable_
- The in keyword
- An iterable (something consisting of a collection of values, e.g. a list)
- A colon
- A code block, starting on the next line

````
teletubbies = ['Tinky Winky', 'Dipsy', 'La La', 'Po']
for name in teletubbies:
  print(name)
````

Like while loops, the for loop can also use the `break` and `continue` statements.

#### `range` function

One very common use of the for loop is to iterate over a range of numbers, and this is done using the built-in `range` function. The `range` function lets you specify a starting number and an ending number, and will iterate over all numbers between them — including the start number, but _not_ including the end number.

````
for index in range(0, len(teletubbies)):
  print('The Teletubby at index ' + str(index) + ' is ' + teletubbies[index])
````

#### `enumerate` function

If you need to refer to the index of each element as well as the element itself, you can use the `enumerate` function:

````
for index, value in enumerate(teletubbies):
  print (index, ": ", value)
````

#### List Comprehension

As an alternative to the `for`, list comprehenstion can be used as a more declarative, easier to read and understand shorthand:

`[print(name) for name in teletubbies]`

### Try, Except and Finally

Try, `except` and `finally` are synomous with `try...catch` in other languages, where the `except` block is executed if the try block raises an error. The `except` block can catch all or specific errors. If present, the `finally` block is always executed.

````
number = 12
try:
  msg = 'hello' + number # TypeError is raised
except:
  print('Something went wrong!') # TypeError is caught and except block is executed

try:
  msg = 'hello' + number # TypeError is raised
except TypeError:
  print('Something went wrong!') # TypeError is caught and except block is executed
finally:
  print('Exiting the try block') # Always executed

dict = {}
try:
  dict['Apple'] # KeyError is raised
except TypeError:
  print('Something went wrong!') # This block only catches TypeError so is skipped
finally:
  print('Exiting the try block') # Always executed - the original KeyError would be raised

exiting the try block
Traceback (most recent call last):
File ".\greeting.py", line 6, in <module>
dict['Apple']
KeyError: 'Apple'
````

#### Error Types

- Syntax errors: this is where code isn't valid Python
- Type errors: this is where the type of some data does not fit what is expected from a function or operator — e.g. when trying to add a number to a string: 'hello' + 12

## Functions

At its simplest, a function definition consists of the following, in order:

- The `def` keyword
- A name for the function
- A pair of parentheses
- A colon
- A code block, starting on the next line

You can add a _default value_ with `=` when declaring the parameters in the definition. Note, a non-default argument cannot follow a default argument.

you to send arguments using `key = value` syntax, called _keyword arguments_ (as opposed to _positional arguments_). Keyword arguments can also be specified in any order. Functions can be called with a mix of positional and named arguments

````
def print_item(name, price_in_pennies = 100):
  formatted_price = '£{:.2f}'.format(price_in_pennies / 100.0)
  print('Item: ' + name)
  print('Price: ' + formatted_price)

print_item('Milk', 85)
print_item('Coffee', 249)
print_item('Orange Juice', 110)
print_item('Eggs') # default price
print_item(price_in_pennies = 1999, name = 'Jamesons') # keyword arguments (unordered)
print_item('Cat Food', price_in_pennies = 149) # mix of positional and named arguments
````

_Note: If you call the above with the wrong amount of arguments you'll see an error like:_

_`TypeError: greet_user() takes exactly 2 arguments (1 given)`_

### Returning data

Functions can return data with the `return` statement.

````
def square(number) -> int: # return type hint - ignored by the interpreter
  return number * number

result = square(5)
print(result)
print(square(3))
````

_Note: An empty return will return `None`, similar to `null`. It's shorthand for `return None`_

## Note To Read Later
- tuple
- magic methods
- more on arrays
- classes
- decorator syntax: https://book.pythontips.com/en/latest/decorators.html
- keyword arguments: https://treyhunner.com/2018/04/keyword-arguments-in-python/