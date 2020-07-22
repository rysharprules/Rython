# Rython

`Ryan + Python = Rython`

<img src="img/logo.png" alt="Python" width="120"/>

## Prerequisites

You need Python on your machine. You can download the latest version of Python from [here](https://www.python.org/downloads/). 

## How to use the code

Code is situated within the `rython` folder into subfolders `examples` and `exercises`:

````
RYTHON
│   README.md
│   ...
└───rython
    │
    └───examples
    │       ...
    └───exercises
        │   ...
        └───fizzbuzz
                fizzbuzz_1.py
                fizzbuzz_2_stretch.py
````

- **examples**: Tend be one-off samples of code taken or expanded from the notes.
- **exercises**: Course specific exercises, contained within their own folders. Any extra required files will also be contained within these folders unless specified. There may be multiple implementations based on the steps, e.g. `fizzbuzz_1.py` is the solution to FizzBuzz, step 1. Stretch tasks are denoted by `_stretch` in the filename and again, may include multiple steps as per the exercise.

To run a file, either run in your preferred IDE, or open a command line, `cd` to the appropriate directory and run the `.py` file with `python`, e.g.:

````
cd rython\exercises\fizzbuzz
python fizzbuzz.py
````

_Note: Use forward slash for Unix/Mac `/` between folders when changing directory._

## Notes

1. [Fundamentals](https://github.com/rysharprules/Rython/blob/master/01_fundamentals.md)
1. [Libraries and the Flask web framework](https://github.com/rysharprules/Rython/blob/master/02_libraries.md)
1. [Input/Output](https://github.com/rysharprules/Rython/blob/master/03_io.md)
1. [Object Oriented Programming](https://github.com/rysharprules/Rython/blob/master/04_oop.md)