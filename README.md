# Rython
Ryan's Python learning materials

- [Rython](#rython)
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
    - [Dictionary](#dictionary)
      - [Accessing individual items](#accessing-individual-items)
      - [Adding to and modifying](#adding-to-and-modifying)
      - [Removing items](#removing-items)
      - [Length](#length-2)
    - [Set](#set)
  - [Note To Read Later](#note-to-read-later)

## Installation

You can download the latest version of Python from [here](https://www.python.org/downloads/). 

_Note: Version **3.8.3** was used in this course._

## Basics

check the [Python documentation](https://docs.python.org/3/) to clarify how a given feature works.

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

You would need to explicitly cast the number to a string using the `str()` function before it can be
added:

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
>>> original_string =
'Supercalifragilistic'
>>> original_string[0:5] # 'Super'
>>> original_string[5:9] # 'cali'
>>> original_string[:5] # 'Super'
>>> original_string[9:] #
'fragilistic'
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

## Note To Read Later
tuple
`in`
magic methods
more on arrays
classes