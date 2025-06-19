# Conditional Logic and Loops
## Learning Objectives:

* Boolean logic (`True` and `False`).
* Conditional statements (`if`, `else` and `elif`).
* `for` and `while` loops.

## Overview

So far we have only considered linear programs (sequence). However, programs can have different structures:

![logic_loop](../pictures/logic_loop.png)

Depending on condition we run different parts of the program (choice). We can also repeat sections of the program (Loop/Repetition).

### Conditional logic

In programming languages the Boolean logic formalism is used to make decision or choices. It consists of:

- Relational operators: greater than, less than, equal to, etc.
- Logical operators: AND, OR, NOT and (exclusive-or: XOR).

#### Relational operators

Relational operators in Python are:

| Symbol | Relational operation |
|:------:|:--------------------:|
| `<`    | Less than |
| `>`    | Greater than |
| `<=`   | Less than or equal to|
| `>=`   | Greater than or equal to|
| `==`   | Equal to (this is different to `=`, which <br> means a variable takes on a new value)|
| `!=`   | Not equal to |

```python
3 < 5   # compares 3 with 5
True    # statement correct: True

3 > 5   
False   # statement incorrect: False
```

#### Logical operators

We can combine expressions with Boolean logical operators: AND, OR, NOT and XOR. The Boolean operator XOR is rarely used, but included for completeness. In python depending how they can be used there are _symbol_ and _word_ or either _symbol_ or _word_ available:

| _symbol_ | _word_ | Boolean logical operator |
|:--------:|:----------:|:-------------:|
| `&`      | `and`      | AND|
| `\|`     | `or`       | OR |
|| `not` | NOT |
| `^`    | | XOR |

To use _symbol_ or _word_ it is up to your preference, but it also depends what is used in the programming language you have learned first. In python program code `and`, `or` and `not` are usually used instead of their symbols, as it closer to our written language.

The function of the logical operators can be summarised by 'truth tables', showing input and output values from a particular function.

##### Logical operator AND 

Do you like pizza?

`and`

Do you like pineapple on it?

| Input A | Input B | A `and` B|
|:-------:|:-------:|:--------:|
| False   | False   | False    |
| True    | False   | False    |
| False   | True    | False    |
| True    | True    | True     |
| I like pizza | I like pineapple | Answer|

##### Logical operator OR

Do you like this class?

`or`

Do you not like this class?

| Input A | Input B | A `or`  B|
|:-------:|:-------:|:--------:|
| False   | False   | False    |
| True    | False   | True     |
| False   | True    | True     |
| True    | True    | True     |

##### Logical operator XOR

You have a bag of green, blue, red, purple, orange and yellow marbles. You want to draw 1 yellow and 1 green marble:

| Input A | Input B | A `^`   B|
|:-------:|:-------:|:--------:|
| False   | False   | False    |
| True    | False   | True     |
| False   | True    | True     |
| True    | True    | False    |
| Yellow  | Green   | Result   |

##### Logical operator NOT

I do (`not`) like pizza.

| Input A | `not`(A) |
|:-------:|:--------:|
| False   | True     |
| True    | False    |

This can be combined with `and`, .`or` and `^` (xor):
- `not`(A `and` B)
- `not`(A `or` B)
- `not`(A `^` B)

##### Examples

Scalars:

```python
x = 5
x > 3
True
x < 3
False
(x > 3) or (x < 3)
True
```

Arrays: 

```python
import numpy as np
A = np.array([1,2,3,4,5])

A > 3
array([False, False, False,  True,  True])

A < 3
array([ True,  True, False, False, False])
```

When using arrays, you need to be a bit careful. For example, it is not clear to python, if you want to compare the array or an element of the array. The following example will rase an error:

```python
(A > 3) or (A < 3)
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
```

To perform an element comparison use the _numpy_ logical operators:

- `np.logical_and()`
- `np.logical_or()`
- `np.logical_xor()`
- `np.logical_not()`

```python
np.logical_or(A > 3, A < 3)
array([ True,  True, False,  True,  True])
```

To check, if an array contains a specific value, you can use the following:
```python
5 in A
True
```
### Conditions and `if` statements

The `if` statement is a conditional statement. It is used to execute a block of instructions (statements) only when a specific condition is :

- `if` statements can have a series of conditions.
- The first condition to be satisfied causes one or more statements/instructions to be executed.
- All following statements in the `if ` construction are skipped.
- There are 3 blocks, that can build an `if` construction:
    - `if`
    - `elif` short for _else if_
    - `else`

An `if` construction always starts with `if` followed by `elif`, `else` or nothing. An `if` construction can as many `elif` conditions as you want, but there is always one `if` and utmost one `else`.

```python
x = 3
if x > 2:
    print('x greater than 2')
elif x = 2:
    print('x is equal to 2')
else:
    print('x is lower than 2')
```

### Indentation

Python relies on indentation (whitespace at the beginning of a line) to define blocks or connected parts in the code. Other programming languages often use curly-brackets `{}` for this purpose or and `end`, if the block or construction is over.

:::{warning}

An `if` statement, without indentation will raise an error:
```python
if x > 2:
print('x greater than 2') # will raise error message
```
:::

### Loops: `for `and `while`


