# Fitting Data
## Learning Objectives:

* Spline and polynomial fit.
* Fitting data and derive parameters.
* Goodness of fit: $R^2$-value.

## Overview

Data fitting including polynomial, spline or more general curve fitting or model is a fundamental process in many fields, including science, engineering, economics and data science. Its core purpose is to find a mathematical function or model that best describes the relationship between variables/parameters in a given set of data points.

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
    * **Identifying Relationships:** Even in the absence of a complete theoretical model, data fitting can reveal correlations and relationships between different material properties or processing parameters. This can guide the development of new materials or optimisation of existing ones.

This session focuses on polynomial and spline fitting.

## Polynomial fitting

Polynomial fitting is a widely used technique in Materials Science to model experimental data and understand underlying relationships between variables. 

### What is Polynomial Fitting?

Polynomial fitting or polynomial regression involves finding the coefficients of a polynomial function that best approximates a set of given data points. The general form of a polynomial is:

$y = a_0 + a_1x + a_2x^2 + \dots + a_nx^n$

where $y$ is the dependent variable, $x$ is the independent variable, $a_0, a_1, \dots, a_n$ are the coefficients to be determined and $n$ is the degree of the polynomial. Polynomial fits are use 

  * **Determining Physical Parameters:** The coefficients of the fitted polynomial can sometimes be directly related to physical constants or properties, allowing for their determination from experimental measurements. For example, you have data of Voltage and Current. By fitting a linear polynomial to the data you are able to determine the resistance (Ohm's law: $V=R\cdot I$). 
  * **Noise Reduction/Smoothing:** Experimental data often contains noise. Polynomial fitting can smooth out these fluctuations, revealing the underlying trend.
  * **Interpolation and Extrapolation:** Once a polynomial fit is obtained, it can be used to estimate values between known data points (interpolation) or predict values beyond the range of the observed data (extrapolation). However, extrapolation with polynomials, especially high-degree ones, can be risky and the curve can wildly oscillate outside the data range.
  * **Simplifying Complex Models:** Materials science often deals with complex phenomena. The complexity of the model might be approximated by a simpler polynomial for ease of calculation or analysis within a specific range allowing to describe observed relationships without necessarily understanding the fundamental physical laws in detail.

### Methods for Polynomial Fitting:

The most common method for polynomial fitting is **Least Squares (LS)**.

  * **Ordinary Least Squares (OLS):** This method minimises the sum of the squares of the vertical distances (residuals) between the data points and the fitted polynomial curve. It assumes that the errors are primarily in the dependent variable ($y$) and are normally distributed with constant variance (this semester).
  * **Total Least Squares (TLS) and Orthogonal Distances (OD):** These methods are more advanced and consider errors in both the $x$ and $y$ variables, which can be more realistic for some experimental setups. They minimise the orthogonal distance from the data points to the fitted curve. While more robust in certain scenarios, they are computationally more complex than OLS (next semester).

### Considerations and Challenges:

  * **Choosing the Degree of the Polynomial ($n$):** This is a crucial step.
      * **Underfitting:** A low-degree polynomial might not capture the true complexity of the data, leading to a poor fit.
      * **Overfitting:** A high-degree polynomial (especially one close to the number of data points) can fit the noise in the data rather than the underlying trend. This results in a curve that passes through most points but may wildly oscillate between them, leading to poor generalisation and extrapolation.
      * **Strategies for choosing degree:**
          * **Visual inspection:** Plotting the data and trying different degrees can give an initial idea.
          * **Physical intuition:** The expected physical relationship might suggest a certain polynomial degree (e.g., quadratic for constant acceleration).
          * **Statistical measures:** $R^2$ or R-squared (used in this session), adjusted $R^2$ or Bayesian Information Criterion can help evaluate the goodness of fit.
  * **Uncertainty and Error Propagation:** In Materials Science, it's essential to consider the uncertainties in the measurements and how they propagate to the fitted parameters. Least squares methods can provide estimates of the uncertainties in the fitted coefficients.

To fit data with a polynomial we can use the function `np.polyfit()` from the Numpy package. It requires three inputs:

- `x`: 1D array of x-coordinates (independent variable).
- `y`: 1D array of y-coordinates (dependent variable).
- `deg`: degree of the fitting polynomial.

`np.polyfit()` returns the coefficient `p` of the polynomial. To evaluate the polynomial fit the `np.polyval()` function is used, which takes the

- `p`: 1D array of polynomial coefficients from highest degree to the constant term.
- `x`: A number or 1D array of numbers at which to evaluate `p`.

as inputs and returns number or 1D array of numbers.

```python
import numpy as np
import matplotlib.pyplot as plt

x_data = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])  # some x data
y_data = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])  # some y data

p3 = np.polyfit(x_data, y_data, 3)   #fits polynomial of degree 3 to the data and returns coefficient
print(p3)  # prints coefficients
p30 = np.polyfit(x_data, y_data, 30) # overfitting the data for illustrational purpose. It should return also a warning message.
print(p30)  # prints coefficients

x_new = np.linspace(min(x_data)-1, max(x_data)+1, 100) # creates new x data where fits are evaluated
y_p3 = np.polyval(p3, x_new)   #evaluates p on new x
y_p30 = np.polyval(p30, x_new) #evaluates p on new x

# Plot the data and the fitted curves
plt.plot(x_data, y_data, 'ko', label='Original Data')
plt.plot(x_new, y_p3, 'b-', label='Polynomial of degree 3')
plt.plot(x_new, y_p30, 'r--', label=f'Polynomial of degree 30')
plt.xlabel('X')
plt.ylabel('Y')
plt.ylim((-1.5,2))
plt.legend()
plt.show()
plt.close()
```

Polynomial fitting is a useful and versatile tool for analyzing and interpreting experimental data. However, careful consideration of the polynomial degree (potential for overfitting) and numerical stability is crucial for obtaining meaningful and reliable results.

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
     & = & \frac{y_2 - y_1}{x_2 - x_1} \cdot x & + & y_1 - \frac{y_2 - y_1}{x_2 - x_1} \cdot x_1\\
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

with the additional condition that the first and second derivative of polynomial $s_{i-1}(x_i)$ (e.g. for $i=1$ the piecewise polynomial for points ($x_0, y_0$) and ($x_1, y_1$)) at the point ($x_i, y_i$) is equal to the first and second derivative of polynomial $s_{i}(x_i)$ (e.g. for $i=1$ the piecewise polynomial for points ($x_1, y_1$) and ($x_2, y_2$)) at the point ($x_i, y_i$). Or in mathematical notation:

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

plt.plot(x_data, y_data, 'ko', label='Original Data')
plt.plot(x_new, y_CubicSpline, 'b-', label='CubicSpline (cubic spline)')
plt.plot(x_new, 1.5**x_new, 'r--', label=f'$y=1.5^x$')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
plt.close()
```

:::{Warning}

Extrapolation must be done with caution as fits can diverge rapidly outside the fitted range.

:::

More details with examples on extrapolating data can be found <a href="https://docs.scipy.org/doc/scipy/tutorial/interpolate/extrapolation_examples.html" target="_blank">here</a>.  If you only want to know more about the impact of different boundary condition on extrapolating data using CubicSpline, you can scroll down to <a href="https://docs.scipy.org/doc/scipy/tutorial/interpolate/extrapolation_examples.html#cubicspline-extend-the-boundary-conditions" target="_blank">here</a>. 


## Coefficient of determination: $R^2$

The Coefficient of Determination, denoted as $R^2$ or R-squared, is a crucial statistic in regression analysis. $R^2$ is a measure of the "goodness of fit" of your model (fitting function). In simpler terms, it indicates how well the fitted line to the data approximates the actual data points. 

If you look at the fit to your data, there's a total amount of variation in the dependent variable (y-values, the thing you're trying to predict). $R^2$ tells you what percentage of that total variation can be "explained" or "accounted for" by the independent variables in your model (fitting function).

$R^2$ values always fall between 0 and 1 (or 0% and 100%):
* **$R^2 = 0$**: This means the model explains none of the variability in the dependent variable.
* **$R^2 = 1$**: This indicates that the model perfectly predicts the outcome. All the variation in the dependent variable is accounted for by the independent variables. In real-world data, an $R^2$ of 1 is very rare, as there's almost always some unexplained variability.
* **$0 < R^2 < 1$**: The model partially explains the outcome. For example, an $R^2$ of 0.75 means that 75% of the variation in the dependent variable can be explained by the independent variables in your model, while 25% remains unexplained.

A good fit should account for approximately 95% or more of the data $(R^2>0.95)$.


### Calculation of $R^2$

$R^2$ is calculated as:

$R^2 = 1 - \frac{\text{Sum of Squared Residuals (SSR)}}{\text{Total Sum of Squares (TSS)}} = 1 - \frac{J}{S}$

where:
* **Sum of Squared Residuals (SSR)** (also defined as $J$): This measures the variability of the data points around the regression line (fit). It's the sum of the squared differences between the actual observed values ($y_i$) and the values predicted by the model ($\hat{y_i}$, best fit function $f(x)$ evaluated at your independent variable x).

    $SSR = J = \sum_{i=1}^{n} (y_i - \hat{y_i})^2$

* **Total Sum of Squares (TSS)** (also defined as $S$): This measures the total variability in the dependent variable around its mean. It's the sum of the squared differences between the actual observed values ($y_i$) and the mean of the dependent variable ($\bar{y}$).

    $TSS = S = \sum_{i=1}^{n} (y_i - \bar{y})^2$