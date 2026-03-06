import numpy as np

def model_func(x, a, b):
    return a*x**3 + b*x

x_data = np.linspace(-2, 2, 20)
y_true = model_func(x_data, 0.75, -1.5)
y_err = 0.2 + 0.2 * np.random.rand(20) # Random uncertainties
y_data = y_true + np.random.normal(0, y_err)
x_err = 0.1 + 0.1 * np.random.rand(20)
x_data = x_data + np.random.normal(0, x_err)

np.savetxt('task5.csv', np.c_[x_data,x_err,y_data,y_err],fmt='%.2f', delimiter=',',header='x_data,x_err,y_data,y_err')
