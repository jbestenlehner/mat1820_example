# Reading and writing files

## Learning Objectives:

* Reading and writing files.
* Built in functions `open()` and `write()`
* Numpy's `np.loadtxt()` and `np.savetxt()`
* Pandas' `DataFrame`

## Overview

Colab is a web-based cloud-service hosted by Google accessible via a web-browser. Therefore, any files you would like to read needs to be uploaded to Colab workspace of your session. Files you create or write to are stored on your workspace of your Colab session. Those files are only temporarily stored. If you close your session (e.g. closing browser tab), all your data and files will be lost.

There are many ways you can access data from or within a Colab session, but we will only use the following.

### Uploading files from Blackboard

The Colab cloud-service uses Linux. So Linux commands can be used to handle data. To upload data from Blackboard or website in general you can use the command `wget`. Linux commands within your code cell are executed with a "!" in front of the command.

```bash
!wget <link>
```

`<link>` is the place holder for the web link, e.g. https://github.com/jbestenlehner/mat1820_example/blob/main/data/somefile.txt

```bash
!wget https://github.com/jbestenlehner/mat1820_example/blob/main/data/somefile.txt #uploads the file to your Colab session
!ls               # lists files in your Colab session
!cat somefile.txt # shows the content of your file
```

### Uploading and downloading local files

To uploaded and download local files Google provides a python package 

## Reading and writing text files

Python provides built-in functions for creating, writing, and reading files.

### Creating a new files

To create a new file in Python, the function `open()` is used with one of the following parameters:

- `'w'` - writes - : `open('myfile.txt', 'w')` will create a new file if the specified file does not exists or **overwrite** an existing file.
- `'a'` - append - : `open('myfile.txt', 'a')` will create a new file if the specified file does not exists or **append** to an existing file.
- `'x'` - create - : `open('myfile.txt', 'x')` will create a new  file or returns an error if the file exists.

Note: files are temporarily created and written to your Colab session. They will be lost, if you close the session.

### Reading a file line by line

To open a file in _read only_ the parameter `'r'` is used with the function `open()`. 

```python
!wget https://github.com/jbestenlehner/mat1820_example/blob/main/data/somefile.txt #uploads the file to your Colab session
file = open('somefile.txt', 'r')
```
This creates an iterable object and we can read in the file line by line with a loop:

```python
for line in file: # reads the file line by line
    print(line)   # prints each line
file.close()      # closes the file
```
The `\n` at the end of the line indicates a new line as discussed in the previous tutorial in session 4.

The following example shows how to read file, creates list of its content and converts the list into a numpy array.  The example uses the function `.strip()` which returns a copy of the string with leading and trailing whitespace removed including new line (`\n`) and the function `.split()`, which returns a list of the substrings in the string, using `sep` as the separator string. If no separator string is given, the string will split on any white space character including new line (`\n`) and tab (`\t`).

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

Note: `.split()` is mainly useful for data that has been intentionally delimited.

### Writing to a file

Before we can write into a file we need to create it first, e.g. `open('myfile.txt', 'w')` (see [creating a new file](#creating-a-new-files)).

```python
file = open('myfile.txt', 'w')           # creates a new file called myfile.txt or overwrites it, if it already exists.
for i in range(1,4):                     # produces range 1, 2, 3
    a_string = (f'Line {i+1:.0f}\n')     # creates a string and formats indexes i into string 
    file.write(a_string)                 # writes string into file
file.close()                             # closes the file
```

Note: `'\n'` (new line) needs to be added at the end of the string. Unlike `print()` the `.write()` function does not add by default a `\n` to the end of the string. If `\n` is not added, all strings will be written into the same line.

:::{warning}

File must be closed after writing the data, e.g. `file.close()`. If the file is not closed properly, not all data might be written to the file.

:::

## Numpy: reading and writing text files

