# Reading and writing files

## Learning Objectives:

* Reading and writing files.
* Built in functions `open()` and `write()`
* Numpy's `np.loadtxt()` and `np.savetxt()`
* Pandas' `DataFrame`

## Overview



### Reading and writing text files

Python provides built-in functions for creating, writing, and reading files.

#### Creating a new files

To create a new file in Python, the function `open()` is used with one of the following parameters:

- `'w'` - writes - : `open('myfile.txt', 'w')` will create a new file if the specified file does not exists or **overwrite** an existing file.
- `'a'` - append - : `open('myfile.txt', 'a')` will create a new file if the specified file does not exists or **append** to an existing file.
- `'x'` - create - : `open('myfile.txt', 'x')` will create a new  file or returns an error if the file exists.

#### Reading a file line by line

To open a file in _read only_ the parameter `'r'` is used with the function `open()`. 

```python
file = open('somefile.txt', 'r')
```
This creates an iterable object. We can read in the file line by line with a loop:

```python
for line in file: # reads the file line by line
    print(line)   # prints each line
file.close()      # closes the file
```
The `\n` at the end of the line indicates a new line. See tutorial for more details.

The following example shows how to read file, creates list of its content and converts the list into a numpy array.  The example uses the function `.strip()` which returns a copy of the string with leading and trailing whitespace removed including new line (`\n`) and the function `.split()`, which returns a list of the substrings in the string, using `sep` as the separator string. If no separator string is given, the string will split on any white space character including new line and tab.

```python
import numpy as np

file = open('somefile.txt', 'r') # opens file in read-only.
data = []                        # creates and empty list
for line in file:                # reads the file line by line
    line = line.strip()          # strips leading and trailing whitespace
    line = line.split()          # splits the string into substrings at each white space
    data.append(line)            # appends the list line to the list data
data = np.array(data)            # converts list to numpy array
print(data.shape)                # shape of array in lines and columns
print(data)
```

Note, `.split()` is mainly useful for data that has been intentionally delimited.

#### Writing to a file

Before we can write into a file we need to create it first, e.g. `open('myfile.txt', 'w')` (see [creating a new file](#creating-a-new-files)).

```python
file = open('myfile.txt', 'w')           # creates a new file called myfile.txt or overwrites it, if it already exists.
for i in range(1,4):                     # produces range 1, 2, 3
    a_string = ('Line ' + str(1) + '\n') # creates a string and converts indexes i into string 
    file.write(a_string)                 # writes string into file
file.close()                             # closes the file
```

Note: `'\n'` (new line) needs to be added at the end of the string. Otherwise all strings will be written into the same line.

:::{warning}

File must be closed after writing the data, e.g. `file.close()`. If the file is not closed properly, not all data might be written to the file.

:::