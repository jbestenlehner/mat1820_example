# Symbolic mathematics
## Learning Objectives:

* Numerical methods: numerical and symbolic
* Integrations and differentiation.
* Simplification and solving equations.

## Overview

There are a couple of libraries or packages available for symbolic mathematics in Python. In this course we will use <a href="https://www.sympy.org/en/index.html" target="_blank">**SymPy**</a>. It's a powerful, open-source library that allows you to perform a wide range of mathematical operations symbolically, rather than numerically. This means it manipulates mathematical expressions in their exact form, preserving variables and functions, instead of approximating them with floating-point numbers.

SymPy is fairly straightforward to use and comes with an extensive <a href="https://docs.sympy.org/latest/index.html#" target="_blank">documentation</a> including <a href="https://docs.sympy.org/latest/tutorials/index.html#tutorials" target="_blank">tutorials</a>.

### Why use Symbolic Math?

  * **Exact Solutions:** Obtain precise answers to mathematical problems, not just approximations.
  * **Understanding Relationships:** See how variables and parameters affect the outcome of an expression or equation.
  * **Derivations and Proofs:** Ideal for deriving formulas, proving identities, and exploring mathematical relationships.
  * **Code Generation:** Generate code for numerical computations from symbolic expressions.


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


 **Basic Usage Example:**

```python
import sympy as sp

# Define symbolic variables
x, y = sp.symbols('x y')

# Create an expression
expr = (x + y)**2

# Expand the expression
expanded_expr = sp.expand(expr)
print(f"Expanded expression: {expanded_expr}")

# Differentiate the expression with respect to x
derivative_x = sp.diff(expr, x)
print(f"Derivative with respect to x: {derivative_x}")

# Solve an equation
equation = sp.Eq(x**2 - 4, 0) # x^2 - 4 = 0
solutions = sp.solve(equation, x)
print(f"Solutions to x^2 - 4 = 0: {solutions}")

# Integrate an expression
integral_x_squared = sp.integrate(x**2, x)
print(f"Integral of x^2: {integral_x_squared}")

# Evaluate a definite integral
definite_integral = sp.integrate(x**2, (x, 0, 2))
print(f"Definite integral of x^2 from 0 to 2: {definite_integral}")

# Print a nice representation (requires LaTeX to be installed for full beauty)
sp.init_printing(use_latex='mathjax') # or 'png', 'svg'
print(f"\nPretty print of (x + y)^2: {expr}")
```