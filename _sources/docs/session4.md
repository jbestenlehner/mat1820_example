# Input and output plus data types
## Learning Objectives:

* Understand different data types.
* User defined input and output.
* `for` loops.

## Overview

In programming languages, data type is an important concept as it tells the computer, how much memory space needs to be reserved to store a value. Python is a dynamically-typed language, which means you don't have to explicitly declare the data type of a variable when you create it. It is inferred when you execute your code at runtime.

Variables can store data of different types, and different types used for different things.

The following data types are used for this course and built in by default in python:

- _Text type_: string: `str`, python does not have a character type like other programming language. A character is a string of length 1. 
- _Numeric Types_: integer: `int`, floating value `float` and complex numbers: `complex`.
- _Sequence Types_: list `[]`, tuple `()`, `range`
- _Boolean Type_: `bool`: `True` or `False`. See next [session](#session5).

There are more data types in python like Mapping Type (dictionaries) or Set Types (storing multiple items in a single variable). An overview of the different built-in types can be found <a href="https://docs.python.org/3/library/stdtypes.html" target="_blank">here</a>.

### List `[]`, tuple `()` and numpy arrays

You might have been unaware, but we already used lists and tuples:

```python
import matplotlib as plt
import numpy as np
a = (1, 2, 3)           # this is a tuple
plt.xlim((1, 5))        # the tuple (1, 5) sets the range of the x-axis
b = [1, 2, 3]           # this is a list
c = np.array([1, 2, 3]) # this is a numpy array
```

While lists and tuples can contain different data types numpy arrays except either `int`, `float`, `complex` or `str`. 

```python
a = (1, '5', 2.3)
b = [1, '5', 2.3]
c = np.array([1, '5', 2.3]) # converts all data types to type string.
c = c.astype(float)         # assigns new type float to array. Note: this will raise an error, if there are letters.
c = np.array([1, '5', 2.3], dtype=float) # equivalent to above, but you tell numpy what dtype (short for data type) the array should have.
```

If you don't what type your variable is, you can use the `type()` function.

```python
type(a)
tuple
type(b)
list
type(c)
numpy.ndarray
x = 5
type(x)
int
```

Lists and tuples have similar properties, but you cannot assign a value to a list.

```python
a = (1, '5', 2.3)
a[0] = 2  # raises the error: TypeError: 'tuple' object does not support item assignment
b = [1, '5', 2.3]
a[0] = 2  # assigns the value 2 to the first element of the list [2, '5', 2.3]
```

You can change between types by using `list()`, `tuple()` or `np.array`:

```python
import numpy as np
a_list = [1, 2, 3]
a_tuple = tuple(a_list)
a_nparray = np.array(a_tuple)
a_list_again = list(a_nparray) 
```

### Repetitive Tasks: `for` loops

`for` loops are used when you have a block of code which you want to repeat a fixed number of times. The `for`-loop is used in combination with an _iterable_ object (often sequence type) such as `list`, `tuple`, `range`, `dictionary`, `set`, or a `string`. For example:

```python
a_list = [1, 2, 3]      # Creates a list
for element in a_list:  # for loop syntax
    print(element)      # prints 1, 2 and 3

```
`a_list` is the _iterable_ object while `element` is the variable where the elements of `a_list` are assigned to.

Note: The end of the `for` statement is indicated by a `:`. In the next line follow instruction/statements, which are indented like bullet points. Python relies on indentation (whitespace at the beginning of a line) to define blocks of code.

:::{warning}

A `for` loop without indentation will raise an error:
```python
for element in a_list: # for loop statement
print(i)   # will raise error message
```
:::

You can also iterates over strings:

```python
word = 'Materials'
for letter in word:
    print(letter)
```

#### Sequence: `range()`

The function `range()` produces a sequence of integers from `start` (inclusive) to `stop` (exclusive) by `step` (default step size is 1), e.g. `range(3)` produces 0, 1, 2. The `start` default is 0 and `stop` is 3 omitting 3. 

`range(0,3)` is equivalent to `range(3)`.

The third parameter is the `step` size: `range(1,6,2)` produces 1, 3, 5 while `range(1, 5, 2)` produces 1, 3 *omitting* `stop`.

```python
for i in range(3):
    print(i)
```

From previous session you might remember the numpy function `np.arange`. At a first glance `range` and `np.arange` seemed to be doing the same thing. 

```python
import numpy as np
for i in np.arange(3):
    print(i)
```

However, `np.arrays` should be avoided when used only for indexing or counting. Because Python creates a physical copy in memory of the numpy array (`np.arange(3)`) and then iterates over it. In the case of `range(3)` the integers are 1 by 1 temporally produced.

An indexer `i` over a range is usually used, if you want to update values in a list or array:

```python
a_list = [1, 2, 3]      # Creates a list
for i in range(3):
    a_list[i] = a_list[i]*(i+2) # multiplies each element by i + 2 and assigns the results to the i's element of the list.
```

This will update the list to `a_list = [2, 6, 12]`.