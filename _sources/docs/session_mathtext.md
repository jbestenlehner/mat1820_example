## Writing Mathematical Expressions 

Scientific plots sometimes require writing mathematical expressions. `matplotlib` provides a basic `TeX` implementation called <a href="https://matplotlib.org/stable/users/explain/text/mathtext.html" target="_blank">_Mathtext_</a>, which uses the _LaTeX_ syntax.

You performed a linear fit to a dataset and want to Voltage vs. Current with axes labels and best fit parameter for the Resistance ($R = 5.1 \pm 0.3$).

```python
import matplotlib.pyplot as plt
import numpy as np

#define variables for resistance
resistance = 5.1
resistance_error = 0.3

# create some current and voltage data for plotting
current = np.arange(10)
voltage = resistance*current

plt.plot(current, voltage, 'r-', 
    label='$R = {:.1f} \\pm {:.1f}$ $\Omega$'.format(resistance, resistance_error))
plt.legend()
plt.show()

```
