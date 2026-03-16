# Exercise: $R^2$ and goodness of fit

In session 7 we used $R^2$ (coefficient of determination) to assess the goodness of fit of our model. 

## Task 1 (recap from session 7)

- Load the data from `task1.csv` into Colab. 
- Perform a linear regression by fitting a first order polynomial to this data. 
- Calculate the $R^2$ value. Remember the formula is:

$$
R^2 = 1 - \frac{\text{Sum of Squared Residuals (SSR)}}{\text{Total Sum of Squares (TSS)}} = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y_i})^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}.
$$

- Present your data and fit (e.g. plot) and discuss in a text using the $R^2$-value the goodness of the fit.

## Task 2

There is a data set in `task2.csv` containing the magnetic field ($H$) at set distances ($r$) from a bar magnet. The pole separation ($l$) is 0.1 m. When we calculate the magnetic field strength around a magnet there
are two potential formulas that can be used:

```{math}
:label: monopol
H = \frac{p}{4\pir^2},
```

```{math}
:label: dipol
H = \frac{pl}{4\pir^3}.
```

The first case is for a monopole and the second for a dipole. Depending on the proximity to the magnet and the separation between the poles then either formula can work best for calculating the field strength.

- Fit the data with both equations using a fitting function, that you think is appropriate. When you do this process you should fit a value for the pole strength ($p$) with uncertainties.

- Calculate $\hat{y}$ values (predicted $H$ values from the model) by using the pole strength value you determined and the known pole separation ($l$) at the given $r$ values for your two different fits.

- Using these values calculate a $R^2$ value for each case. 

- Visualise your results and discuss which model can better explain the data?

## Task 3

As you have noticed the file `task2.csv` contains columns with errors for the $H$ and $r$ values:

- Use these values to calculate the pole strength $p$ and propagated error for each data point. Compare the calculated $p$ and error values with your best fit value for $p$ (i.e. either Equation {eq}`monopol` or {eq}`dipol`). If Equation {eq}`dipol` fits your data best, you can assume that the error on $l$ is 0.

- Discuss if the $p$ values agree within the uncertainty range? 

- From above you should have an array with $p$ values. Calculate _mean_, _standard deviation_ and _standard error_ (see Session 10). 

- Discuss if the averaged $p$ value agree within the uncertainties with your best fit value for $p$.

## Task 4

As a general rule when the distance from the magnet is less than the separation of the poles the magnet will normally operate as a monopole (Equation {eq}`monopol`) but when it is greater than or equal to the pole separation it will operate as a dipole.

- Write a code that calculates the magnetic field strength at a set distance (r) from the magnet. The user should supply $p$, $l$ and $r$.

- The code should decide which formula to use to calculate $H$ telling the user if _monopol_ or _dipol_.

- If an invalid number for $p$, $l$ or $r$ is supplied (e.g. a negative number) the code should tell the user the value cannot be calculated by printing an error message to the screen.

- Finally try to modify the code so it can take values for r in a range of units e.g. m, cm, mm, inches, ft and give the correct value.