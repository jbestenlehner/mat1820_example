# Example solutions
## Session 10

### Task 1

Calculate the value of $z$ and error $\Delta z$ for the following problems.

1. $z = x + y$:
    - $x = 15$ and $\Delta x = 0.6$
    - $y = 12$ and $\Delta y = 0.4$

2. $z = x^3$:
    - $x = 6$ and $\Delta x = 0.3$
3. $z = \exp(4x)$:
    - $x = 2.1$ and $\Delta x = 0.1$

Note: see overview page of this session for propagation rules.

Potential Solution:

```python
import numpy as np

# 1.
x = 15
delta_x = 0.6
y, delta_y  = 12, 0.4
z = x + y
delta_z = (delta_x**2 + delta_y**2)**0.5 #if you prefer, you can also use np.sqrt(), np.sqrt(delta_x**2 + delta_y**2)
print('z = {:.0f} +/- {:.1f}'.format(z, delta_z))

# 2.
x, delta_x = 6, 0.3
z = x**3
delta_z = 3*delta_x/x*z
print('z = {:.0f} +/- {:.1f}'.format(z, delta_z))


# 3.
x, delta_x = 2.1, 0.1
z = np.exp(4*x)
delta_z = 4*delta_x*z
print('z = {:.0f} +/- {:.0f}'.format(round(z, -2), round(delta_z, -2)))
```

### Task 3

The file `temperature.csv` contains a range of temperatures and errors in K. Convert the values along with their errors into Celsius.

Potential Solution:

```python
import numpy as np

temp_K, temp_K_err = np.loadtxt('temperature.csv', delimiter=',', skiprows=1, unpack=True)

#Conversion from Kelvin to Celcius
temp_C = temp_K - 273.15
temp_C_err = temp_K_err # constant value is added.
```

Now convert your Celsius values and their errors into Fahrenheit:

$\mathrm{F} =1.8\cdot\mathrm{C} + 32$.

Potential Solution:

```python
temp_F = 1.8*temp_C + 32
temp_F_err = 1.8*temp_C_err
print(np.column_stack((temp_F, temp_F_err))) # prints the arrays, but not asked
```

### Task 5

Find the value and error for the reciprocal of temperatures in K from the file `temperatures.csv` (Task 3). Can you use a function from Task 2 to propagate the error?

Potential Solution:

```python
def power_err(x,delta_x,n):
  """
  propagates error for z = x^n.
  returns delta_z/z
  """
  return np.abs(n)*delta_x/x

temp_rec_K = 1/temp_K
temp_rec_K_err = power_err(temp_K,temp_K_err,-1)*temp_rec_K
#optional print statement to check the result
print(np.column_stack((temp_rec_K, temp_rec_K_err)))
```

## Session 11

### Task 1

In `diffusion.csv` you have a set of data from a diffusion study.

If you look at this data you will see the diffusion values are recorded in $\mathrm{cm^2s^{−1}}$ and the temperature is in Fahrenheit. We are going to need to convert these into SI units i.e. $\mathrm{m^2s^{−1}}$ and $\mathrm{K}$. Hopefully you have ready made examples that you adapt for this from last week.

Potential Solution:

```python
import numpy as np

temp_F, temp_F_err, D_cgs, D_cgs_err = np.loadtxt('diffusion.csv', delimiter=',', skiprows=1, unpack=True)

# convert Fahrenheit to Kelvin
temp_K = (temp_F -32)/1.8 + 273.15
temp_K_err = temp_F_err/1.8

#convert from cgs to SI units
D_SI = 1e-4*D_cgs
D_SI_err = 1e-4*D_cgs_err
```

The movement of atoms in a solid is given by the Arrhenius equation:

$$ 
D = D_0 \exp\left(-\frac{E_A}{k_bT}\right),
$$

where $D_0$ is material dependent constant, $E_A$ is activation energy, $k_B$ is the Boltzmann constant, and $T$ is the temperature in Kelvin and returns the diffusion coefficient $D$.

By taking the natural log of this equation we obtain:

$$
\ln D = \ln D_0 -  \left(\frac{E_A}{k_B T}\right).
$$

1. Take the natural log of the $D$ values and find $1/T$ values.

2. Plot a graph of $\ln D$ (y-axis) and $1/T$ (x-axis). Remember to label your axis. 

3. Perform a linear fit (this is a 1st order polynomial, session 7) and extract a value for $E_A$ (the gradient) and $\ln D_0$ (the constant).

4. Calculate the errors on the $\ln D$ and $1/T$ values following your propagation of error rules. You can use your functions from session 10.

Potential Solution:

```python
import matplotlib.pyplot as plt

# Function for error propagation
def power_err(x,delta_x,n):
  """
  propagates error for z = x^n.
  returns delta_z/z
  """
  return np.abs(n)*delta_x/x

k_B = 1.38e-23 # Boltzmann constant in J/K

#1.
lnD_SI = np.log(D_SI)
temp_rec_K = 1/temp_K
#2.
plt.plot(temp_rec_K, lnD_SI, 'ro', label='Data Points')
plt.xlabel('1/T [K]')
plt.ylabel('lnD [m^2/s]')
plt.legend()
plt.show()
#3.
p = np.polyfit(temp_rec_K, lnD_SI, 1)
E_A = -p[0]*k_B # gradient p[0] = - E_A/k_B
print('E_A = {}, lnD_0 = {} or D_0 = {}'.format(E_A, p[1], np.exp(p[1])))
#4.
lnD_SI_err = D_SI_err/D_SI
temp_rec_K_err = power_err(temp_K, temp_K_err, -1)*temp_rec_K
```

### Task 2

In Task 1 you have hopefully used  <a href="https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html" target="_blank">`np.polyfit()`</a>. If you follow the link or use the help, we will see there is an option to provide Weights as an argument to the polyfit function (`w_i = 1/sigma_i`, see also $\chi^2$ equation). 

**Note:** you can only provide weights for your $y$-data (dependent variable). Next week we will also consider uncertainties on the $x$-data (independent variable).

1. Use `np.polyfit()` with weights on $\ln D$.

2. Compare the value you have extracted for $E_A$ and $\ln D_0$ to the values you found in Task 1.

Potential Solution:

```python
#1.
p1 = np.polyfit(temp_rec_K, lnD_SI, 1, w = 1/lnD_SI_err)
E_A = -p[0]*k_B # gradient p[0] = - E_A/k_B
print('E_A = {}, lnD_0 = {} or D_0 = {}'.format(E_A, p1[1], np.exp(p1[1])))
# 2. Plot for comparison
plt.plot(temp_rec_K, lnD_SI, 'ro', label='Data Points')
plt.plot(temp_rec_K, np.polyval(p,temp_rec_K), 'k-', label='Best fit without errors')
plt.plot(temp_rec_K, np.polyval(p1,temp_rec_K), 'b--', label='Best fit with errors')
plt.xlabel('1/T [K]')
plt.ylabel('lnD [m^2/s]')
plt.legend()
plt.show()
plt.close()
```

### Task 3

Now we have look at the uncertainties on our fitting parameters. To do so we need to access the covariance matrix:

1. `cov=True`: the covariance is scaled. The weights are presumed to be unreliable except in a relative sense and everything is scaled such that the reduced $\chi^2$ is unity.

2. `cov='unscaled'`: if $\sigma$ is a representative estimate of the uncertainty.

If you trust that your errors ($\sigma$) are a true representation of the uncertainties, you set `p, pcov = np.polyfit(x_data, y_data, w=1/sigma_y, cov='unscaled')`.

Potential Solution:

```python
p_3, pcov_3 = np.polyfit(temp_rec_K, lnD_SI, 1, w = 1/lnD_SI_err, cov='unscaled')
```

Above, we stored the covariance matrix in the variable `pcov`. The variance of the parameters are on the diagonal of the covariance matrix => `perr = np.sqrt(np.diag(pcov))`. The covariance matrix is a symmetric matrix ($M=M^{\mathrm{T}}$). Non zero values which are not located on the diagonal mean that parameters are not independent and correlate.

Extract the uncertainty for $E_A$ and $\ln D_0$.

Potential Solution:

```python
perr_3 = np.sqrt(np.diag(pcov_3))
E_A = -p_3[0]*k_B # gradient p[0] = - E_A/k_B
E_A_err = perr_3[0]*k_B
print('E_A = {:.3e} +/- {:.1e}'.format(E_A, E_A_err))
print('lnD_0 = {:.3f} +/- {:.3f}'.format(p_3[1], perr_3[1]))
print('D_0 = {:.3e} +/- {:.1e}'.format(np.exp(p_3[1]), perr_3[1]*np.exp(p_3[1])))
```

### Task 4

Using `curve_fit()` and the exponential form of the Arrhenius equation find $D_0$ and $E_A$ with uncertainties,

$$ 
D = D_0 \exp\left(-\frac{E_A}{k_bT}\right).
$$

Values for $D_0$ and $E_A$ are small (Task 2 and 3). To help `curve_fit()` finding a solution, we can provide <a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html" target="_blank">initial guesses</a> for $D_0$ and $E_A$, e.g. `p0=[1.e-8, 1.e-19]`:

```python
popt, pcov = curve_fit(arrhenius_equation, T, D, sigma=D_err, 
        p0=[1.e-8, 1.e-19], absolute_sigma=True)
```
Compare the values you have extracted for $D_0$ and $E_A$ including uncertainties to the values you found in Task 3.

Potential Solution:

```python
from scipy.optimize import curve_fit

# define arrhenius equation
def arrhenius_equation(T, D_0, E_A):
    """
    Calculates the diffusion using the Arrhenius equation.
    Args:
        T : temperature in Kelvin
        parameters: D_0 and E_A
    """
    k_B = 1.38e-23 # Boltzmann constant in J/K
    D = D_0*np.exp(-E_A/k_B/T)
    return D

# least square fit with curve_fit() with  initial guesses
popt, pcov = curve_fit(arrhenius_equation, temp_K, D_SI, sigma=D_SI_err, 
        p0=[1.e-10, 1.e-20], absolute_sigma=True)
perr = np.sqrt(np.diag(pcov))
# Extract parameters with uncertainties and compare.
print('E_A = {:.3e} +/- {:.1e}'.format(popt[1], perr[1]))
print('D_0 = {:.3e} +/- {:.1e}'.format(popt[0], perr[0]))
print('Task 3 results:')
print('E_A = {:.3e} +/- {:.1e}'.format(E_A, E_A_err))
print('D_0 = {:.3e} +/- {:.1e}'.format(np.exp(p_3[1]), perr_3[1]*np.exp(p_3[1])))
```
Note: Using the exponential form of the Arrhenius equation we do not need to perform error propagations when calculating $D_0$ and $E_A$. However, we need to provide initial guesses of the parameters, as it is numerically less robust to fit than the logarithmic version of the Arrhenius equation.