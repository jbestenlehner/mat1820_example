# Exercise: More data fitting

Analysing and discussing results is an important of your degree. This session will give you another example on fitting data with uncertainties and how to identify and remove outliers in your data set.

## Task 1 
- Read in the data from `session14_task1.csv` into Colab. The data set contains youngs modulus and the mass of a defect added to a sample. Errors are given in the 3rd and 4th column for the data sets. Note that errors are not exactly the same for all data points. These errors should be treated as $\pm$ for each data point, e.g. the 1st point is $4.76 \pm 0.6$ g and $16.20 \pm 0.57$ GPa.

- Plot a graph of the mass of the defect (independent) against youngs modulus (dependent). Add axes labels with units, a legend and error bars for the defect mass and youngs modulus to the graph.

- Use a 1st order polynomial and `odr_fit()` to fit the data with and without errors. Extract out values for m and c with uncertainties for both cases.

- Add the fits to your graph, compare and discuss the results. 

## Task 2

`session14_task2.csv` has a set of data that should make a good linear fit. There is a suspicion that some of the data may be unreliable and should not be used for fitting purposes. 

- Try plotting the data and seeing if you suspect any of the data points look anomalous. 

- Perform a simple 1st order polynomial fit to the data using `np.polyfit()`, extract the parameters with uncertainties and calculate the $R^2$ value of your fit.

- To prove data point is anomalous you need to see if its removal significantly affects the fit and the quality of the fit. To do this you could systemically create new data sets with a data point removed using `np.delete()` and perform a fitting plus $R^2$ calculation. Present and discuss your findings.

- You should be able to automate this process to identify the problematic data point. For example, remove data points, which are 3 to 5 sigma away from the predicted value. Hint: you need to propagate the uncertainties from your best-fit parameters.
