# Symbolic mathematics
## Learning Objectives:

* Numerical methods: numerical and symbolic
* Integrations and differentiation.
* Simplification and solving equations.

## Overview

There are a couple of libraries or packages available for symbolic mathematics in Python. In this course we will use <a href="https://www.sympy.org/en/index.html" target="_blank">**SymPy**</a>. It's a powerful, open-source library that allows you to perform a wide range of mathematical operations symbolically, rather than numerically. This means it manipulates mathematical expressions in their exact form, preserving variables and functions, instead of approximating them with floating-point numbers.

SymPy is fairly straightforward to use and comes with a extensive <a href="https://docs.sympy.org/latest/index.html#" target="_blank">documentation</a> including <a href="https://docs.sympy.org/latest/tutorials/index.html#tutorials" target="_blank">tutorials</a>.

### Why use Symbolic Math?

  * **Exact Solutions:** Obtain precise answers to mathematical problems, not just approximations.
  * **Understanding Relationships:** See how variables and parameters affect the outcome of an expression or equation.
  * **Derivations and Proofs:** Ideal for deriving formulas, proving identities, and exploring mathematical relationships.
  * **Code Generation:** Generate code for numerical computations from symbolic expressions.

### Numerical uncertainties: symbolic vs. numerical

What is the difference between numerically and symbolic operations? Let's consider the example of irrational numbers (the decimal point is non-terminating and non-repeating), e.g. $\pi$ or $\sqrt{2}$ given in their symbolic form. $\pi$ and $\sqrt{2}$ have also a numerical value which is 3.141592653589793... and 1.414213562373095... However, the numerical value is always an approximation, because you cannot write infinite numbers of decimal points.

Note: Symbolic math keeps values in their symbolic rather than numerical form.

In computational modelling there is always a trade off between precision and computational resources like runtime and memory usage. For example, you might have already heard of single and double precision floating-point numbers.  

```python
import numpy as np

#Calculates the square root of 8 numerically
print(np.sqrt(8, dtype=np.float16))  # half-precision floating-point number
print(np.sqrt(8, dtype=np.float32))  # single-precision floating-point number
print(np.sqrt(8, dtype=np.float64))  # double-precision floating-point number (default in Python)
print(np.sqrt(8, dtype=np.float128)) # Extended-precision floating-point number (long double)
```
Even though we have increased the precision, the results are not an exact square root of 8. 

Note: Each increase in precision doubles the memory requirements to store the value and increases the computation time to calculate the square root of 8, which can become a hugh problem for large and complex simulations.

With a symbolic computation system like SymPy provides, the square roots of numbers that are not perfect squares are left unevaluated by default, but symbolic results can be symbolically simplified.

```python
import sympy as sm   #import hte sympy library

print(sm.sqrt(2))
print(sm.sqrt(8))
```

:::[Warning]

Note: You can import packages/libraries as any name you want. The obvious choice is to `import sympy as sp`. However, the SciPy package is usually imported as 'sp', `import scipy as sp` and is more widely used than SymPy.  

:::

The advantage of keeping expression unevaluated is that at some point in your calculation those values might cancel out.

```python
import numpy as np
import sympy as sm

# Numerical calculation of sqrt(2)^4 does not results in the value of 2.
print(np.sqrt(2,dtype=np.float16)**4)
print(np.sqrt(2,dtype=np.float32)**4)
print(np.sqrt(2,dtype=np.float64)**4)
print(np.sqrt(2,dtype=np.float128)**4)

# symbolic calculation provides the exact value of 4.
print(sm.sqrt(2)**4)

expr = sm.sqrt(2)**4
print(expr.evalf())          # numerical evaluation of the symbolic expressions
print(expr.evalf(20))        # numerical evaluation to a precision of 20 digits.

# Another example for pi
print(np.pi)            # double precision
print(sm.pi.evalf(100)) # symbolic pi represents the exact value of pi.
```

Already with the simple example of $\sqrt{2}$ we are able to notice the numerical error.

### Functions of SymPy and applications of symbolic math:

  * **Symbolic Variables:** You can define symbolic variables (e.g., `x`, `y`, `theta`) and work with them algebraically.
  * **Algebraic Manipulation:**
      * **Simplification:** `simplify()`, `expand()`, `factor()`, `trigsimp()`, etc.
      * **Substitution:** Replace symbols or expressions with others using `subs()`.
  * **Calculus:**
      * **Differentiation:** `diff()` for derivatives.
      * **Integration:** `integrate()` for indefinite and definite integrals.
      * **Limits:** `limit()` for evaluating limits.
      * **Series Expansion:** Taylor series, Laurent series.
  * **Equation Solving:** `solve()` for algebraic equations, systems of equations, and even some differential equations.
  * **Linear Algebra:** Operations with symbolic matrices (addition, multiplication, determinants, inverses, etc.).
  * **Discrete Mathematics:** Binomial coefficients, summations, products, number theory functions, logic expressions.
  * **Special Functions:** Support for a wide array of mathematical functions like gamma, Bessel, error functions, etc.
  * **Physics Module:** Tools for symbolic calculations in classical mechanics, quantum mechanics, and more.
  * **Output Formatting:** Can format results as LaTeX code for high-quality mathematical typesetting.