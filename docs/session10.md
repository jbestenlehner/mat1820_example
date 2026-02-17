# Error propagation

When you are conducting experiments, no measurement is perfectly precise. Error propagation is the set of mathematical rules used to determine how the uncertainties in those initial measurements "flow through" to your final calculated result.

In Engineering, we usually represent a value as $x\pm \Delta x​$ or $x\pm \sigma_x​$, where $x$ is the measured value and $​\Delta x​$ is the absolute/approximate error or $\sigma_x​$ is the standard deviation (positive square root of the variance).

## Error propagation Rules

These commons rules are first-order approximation assuming that uncertainties are **independent** and **random** and are small enough so that only the first derivative in a Taylor expansion is significant.

Note: the same rules apply for $\Delta x$ and $\sigma_x$.

### 1. Addition and Subtraction

If your calculation involves adding or subtracting values ($z=x+y$ or $z=x−y$), you add the uncertainties in quadrature:

$$
\sigma_z = \sqrt{\sigma_x^2 + \sigma_y^2}.
$$

Note: Even if you are subtracting the values, the uncertainties always increase. You never subtract errors!

### 2. Multiplication and Division

If your calculation involves multiplication or division ($z=x\cdot y$ or $z=x/y$), you add the relative (fractional) uncertainties in quadrature:

$$
\frac{\sigma_z}{z} = \sqrt{\left(\frac{\sigma_x}{x}\right)^2 + \left(\frac{\sigma_y}{y}\right)^2}.
$$

### 3. Multiplication by a Constant

If you multiply a measurement by a constant that has no uncertainty ($z=C\cdot x$), the uncertainty is simply scaled by that constant $C$:

$$
\sigma_z ​= \sqrt{C^2\,\sigma_x^2} = \lvert C\lvert~\sigma_x​.
$$

### 4. Exponents and Powers

If a variable is raised to a power ($z = x^n$), the relative uncertainty is multiplied by the absolute value of that power:

$$
\frac{\sigma_z}{z} = \sqrt{n^2\left(\frac{\sigma_x}{x}\right)^2} = \lvert n\lvert \frac{\sigma_x}{x}.
$$

If your calculation involves the exponent function ($z=exp(Cx)$), then the estimated error is given by:

$$
\frac{\sigma_z}{z} = \sqrt{C^2\sigma_x^2} = \lvert C\lvert \sigma_x. 
$$

### Why "in Quadrature"?

You might wonder why we use the square root of the sum of squares $\left(\sqrt{\sigma_x^2 + \sigma_y^2}\right)$​ instead of just adding them $(\sigma_x + \sigma_y)$.

Adding them directly assumes the "worst-case scenario" where both errors are at their maximum in the same direction. Using quadrature assumes the errors are **independent** and **random**, meaning it is statistically unlikely that both measurements are off by their maximum amount at the same time.

### 5. Logarithms

When you take the logarithm of a measurement, the rule for error propagation changes quite a bit. Instead of looking at relative uncertainty, the uncertainty of a log function depends on the relative error of the original value.

- Natural Logarithms ($\ln$):

  If your calculation is $z=\ln(x)$, the absolute uncertainty in $z$ is the relative uncertainty of $x$.

  $$
  \sigma_z = \sqrt{\left(\frac{\sigma_x}{x}\right)^2} = \frac{\sigma_x}{x}.
  $$

  This is a unique case where the absolute error of the result is equal to the relative error of the input.

  Assuming independent variables a common formula for error propagation for a function $f(x)$ is:

  $$
  \sigma_f = \sqrt{\left(\frac{\partial f}{\partial x}\right)^2\sigma_x^2}.
  $$

  The derivative for $\ln(x)$ is $\partial \ln(x)/\partial x = 1/x$​ and confirms the rule above.

- Logarithms with base not equal to $e$:
  
  For example, if your calculation is $z=\log_{10}​(x)$, we have to account for the conversion factor between natural logs and base 10 logs:

  $$
  \sigma_z = \sqrt{\left(\frac{1}{\ln(10)}\frac{\sigma_x}{x}\right)^2} = \frac{1}{\ln(10)}\frac{\sigma_x}{x}.
  $$