# Fitting Data
## Learning Objectives:

* Spline and polynomial fit.
* Fitting data and derive parameters.
* Goodness of fit: $R^2$-value.

## Overview

Data fitting, also known as curve fitting or model fitting, is a fundamental process in many fields, including science, engineering, economics and data science. Its core purpose is to find a mathematical function or model that best describes the relationship between variables/parameters in a given set of data points.

Fitting data is often used, but not exclusively:

1.  **Understanding Underlying Relationships and Patterns:**
    * By fitting a model to data, we can uncover the inherent trends and relationships that might not be obvious from raw data. For example, fitting stress-strain curves can determine material parameters like Young's modulus or Poisson's ratio.
    * By fitting data to theoretical or empirical models, we are able to gain a deeper understanding of how materials behave under various conditions (e.g., temperature, stress, chemical environment). This helps us to understand the mechanisms governing material properties and performance.

2.  **Noise Reduction and Smoothing:**
    * Real-world data often contains noise or errors. Fitting a smooth curve to noisy data can help average out these fluctuations, revealing the underlying signal/relations and making the data more interpretable.

3.  **Interpolation and Extrapolation:**
    * **Interpolation:** Using the fitted model to estimate values *within* the range of the observed data points where no data was collected.
    * **Extrapolation:** Using the fitted model to estimate values *outside* the range of the observed data. While useful, extrapolation carries higher uncertainty as the model's behavior outside the observed range might differ.

4.  **Model Validation and Development:**
    * **Testing Hypotheses:** Data fitting is a crucial way to test scientific hypotheses and validate theoretical models. If experimental data closely fits a proposed model, it provides strong evidence for the validity of that model. Conversely, discrepancies can highlight limitations or suggest areas for model refinement.
    * **Developing Predictive Models:** Once a model is validated, it can be used to predict material behavior under conditions that haven't been directly tested, saving time and resources in experimental work. This is particularly valuable in materials design and discovery.
    * **Identifying Relationships:** Even in the absence of a complete theoretical model, data fitting can reveal correlations and relationships between different material properties or processing parameters. This can guide the development of new materials or optimization of existing ones.

## Spline fitting

Spline fitting is a powerful technique for approximating data. Examples for when to use spline fitting are:

1.  **Interpolation:**
    * **Need a smooth curve that passes through *all* data points:** If your data is relatively clean and you need to estimate values between known points.
    * **Examples:**
        * Resampling data to a higher resolution.
        * Fill in missing values within a dataset if the underlying relationship is expected to be smooth.

2.  **Smoothing (Regression Splines/Smoothing Splines):**
    * **Data is noisy:** When your data contains noise or measurement errors, simply interpolating can lead to "wiggles" or overfitting. Smoothing splines aim to find a balance between fitting the data closely and maintaining a desired level of smoothness.
    * **Need to capture non-linear relationships without overfitting:** Splines can model complex, non-linear trends in data more flexibly than a single polynomial, while still avoiding the extreme fluctuations that can arise from high-degree polynomial regression.
    * **Examples:**
        * Trend analysis in time series data.
        * Removing noise from sensor readings.
        * Smoothing out experimental data.

However, this course will focus on point 1.

### What is spline fitting?

Data points are fitting by piecewise polynomials, i.e. neighbouring data points are fitted by different polynomials. Commonly used are polynomial of degree 1 (linear spline) and degree 3 (cubic spline), but any other order can be chosen depending on your data or purpose of fit.

### Linear spline 

Linear splines are used for large datasets when performance is a critical concern or for filling in missing or resampling data where linearity is acceptable. A straight line ($s(x)$) is fitted through 2 data points, e.g. ($x_1, y_1$) and ($x_2, y_2$).

The polynomial is of the form:

$$
\begin{matrix}
s(x) & = & m \cdot x & + & b \\
     & = & \frac{y_2 - y_1}{x_2 - x_1} \cdot x & + & y_1 - \frac{y_2 - y_1}{x_2 - x_1} \cdot x_1
\end{matrix}
$$

Note: $b=y_1-m\cdot x_1$. 

The linear spline interpolation function of numpy is called `np.interp()`. It requires three input parameters:
- `x`: the x-coordinates at which to evaluate the interpolated values.
- `xp`: the x-coordinates of the data points in ascending order (1D array).
- `fp`: the y-coordinates of the data points (1D array).

```python
import numpy as np
import matplotlib.pyplot as plt

# Original data points
x_data = np.array([0, 1, 2, 3, 4])
y_data = x_data**2 # y = x**2

# New points to interpolate at
x_new = np.linspace(0, 4, 20)

# Perform linear interpolation
y_interp_np = np.interp(x_new, x_data, y_data)

plt.plot(x_data, y_data, 'ko', label='Original Data')
plt.plot(x_new, y_interp_np, 'r-', label='np.interp (linear spline)')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
plt.close()
```
Note: `np.interp()` will rase an error when extrapolating data points.

### Cubic spline

As seen in the example above linear splines can be quite inaccurate. Considerable better results provide cubic splines.

The polynomial is of the form

$
\begin{matrix}
s(x) & = & ax^3 + bx^2 + cx + d
\end{matrix}
$

with the additional condition that the first and second derivative of polynomial $s_{i-1}(x)$, e.g. for $i=1$ the piecewise polynomial for points ($x_0, y_0$) and ($x_1, y_1$), at the point ($x_i, y_i$) is equal to the first and second derivative of polynomial $s_{i}(x)$, e.g. for $i=1$ the piecewise polynomial for points ($x_1, y_1$) and ($x_2, y_2$), at the point ($x_i, y_i$). Or in mathematical notation:

$
s'_{i}(x_{i}):=s'_{i-1}(x_{i})
$
and
$
s''_{i}(x_{i}):=s''_{i-1}(x_{i})
$

Numpy does not provide a cubic spline function, but the <a href="https://docs.scipy.org/doc/scipy/reference/interpolate.html" target="_blank">`scipy.interpolate`</a> module of the <a href="https://scipy.org/" target="_blank">SciPy</a> package provides a <a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.CubicSpline.html#scipy.interpolate.CubicSpline" target="_blank">`CubicSpline`</a> function.  It requires two input parameters:
- `x`: the x-coordinates of the data points in ascending order (1D array, independent variable).
- `y`: the y-coordinates of the data points (1D array, dependent variable).

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Original data points
x_data = np.array([0, 1, 2, 3, 4])
y_data = x_data**2 # y = x**2

# New points to interpolate at
x_new = np.linspace(0, 4, 20)

# Perform linear spline interpolation
y_interp_np = np.interp(x_new, x_data, y_data)

# Perform cubic spline interpolation
cs = CubicSpline(x_data, y_data) #creates a function where x_new can be evaluated
y_CubicSpline = cs(x_new)

plt.plot(x_data, y_data, 'ko', label='Original Data')
plt.plot(x_new, y_interp_np, 'r-', label='np.interp (linear spline)')
plt.plot(x_new, y_CubicSpline, 'b--', label='CubicSpline (cubic spline)')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
plt.close()
```

### Extrapolating data with `CubicSpline()`

When extrapolating data we do not have data points at the boundary to full fill the condition above. In our three point example with data points at $i= 0, 1, 2$ we do not have data points at ($x_{-1}, y_{-1}$) and ($x_3,y_3$) to obtain the polynomial $s_{-1}(x)$ and $s_3(x)$, which are required to full fill the condition. Therefore, we need to define a boundary condition, e.g. setting the first derivative to zero ('clamped') or setting the second derivative to zero ('natural'). The default for `CubicSpline()` is when the first and second segment at a curve end are the same polynomial ('not-a-knot').

The optional parameter to the set the boundary condition is called `bc_type`:
- 'not-a-knot': The first and second segment at a curve end are the same polynomial (default).
- 'clamped': The first derivative at curves ends are zero.
- 'natural': The second derivative at curve ends are zero.
- 'periodic': The interpolated functions is assumed to be periodic. For example, we have $n$ data points. The extrapolated data point ($x_{-1},y_{-1}$) is equal to data point ($x_n,y_n$) while the extrapolated data point ($x_{n+1},y_{n+1}$) is equal to data ($x_0,y_0$).

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Original data points
x_data = np.array([0, 1, 2, 3, 4])
y_data = 1.5**x_data # y = 1.5^x

# New points to interpolate at
x_new = np.linspace(-2, 6, 50)

# Perform cubic spline interpolation
cs = CubicSpline(x_data, y_data) #creates a function where x_new can be evaluated
y_CubicSpline = cs(x_new)
y_first_cs = cs(x_new, nu=1)  # calculates first derivative
y_second_cs = cs(x_new, nu=2) # calculates second derivative

plt.plot(x_data, y_data, 'ko', label='Original Data')
plt.plot(x_new, y_CubicSpline, 'b-', label='CubicSpline (cubic spline)')
plt.plot(x_new, y_first_cs, 'y-', label='First derivative')
plt.plot(x_new, y_second_cs, 'g-', label='Second derivative')
plt.plot(x_new, 1.5**x_new, 'r--', label=f'$y=1.5^x$')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
plt.close()
```
More details with examples on extrapolating data can be found <a href="https://docs.scipy.org/doc/scipy/tutorial/interpolate/extrapolation_examples.html" target="_blank">here</a>.  If you only want to know more about the impact of different boundary condition on extrapolating data using CubicSpline, you can scroll down to <a href="https://docs.scipy.org/doc/scipy/tutorial/interpolate/extrapolation_examples.html#cubicspline-extend-the-boundary-conditions" target="_blank">here</a>. 

## Polynomial fitting