# Rython
Ryan's Python learning materials

## Module 1 - General Purpose Coding

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
# Addition
>>> six = 2 + 4

# Subtraction
>>> four = 6 - 2

# Multiplication
>>> twelve = 2 * 6

# Division
>>> eight = 16 / 2

# Power of
>>> twenty_seven = 3 ** 3

# Brackets to change the order of
operations
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