## Pandas: reading and writing data files

Structured data files like `.CSV`, `.JSON`, `.XML`, etc. can contain numerical as well as text data including data labels. For example, a data file might contain names of people (`str`), their ages (`int`) and height (`float`). 'Name', 'Age' and 'Height' are data labels. Of course this can be down with the methods above by using `.split()` or `unpack` and then individually assign the data types to the lists/arrays and define variable according the data contents (name, age, height).

However, there is package called <a href="https://pandas.pydata.org/" target="_blank">pandas</a>, which is a python package develop for real-world Data Analysis. It is able to handle the vast majority of typical use cases in finance, statistics, social science and many areas of engineering providing fast, flexible and expressive data structures designed to make working with relational or labeled data both easy and intuitive. Pandas is able to read many different data files including CSV, JSON, XML, SQL, Excel, HTML, clipboard, etc.

Pandas is imported with

```python
import pandas as pd
```

In this session we mainly use Pandas to read in and out data files. The next semester will focus more on Data Analysis, where we will explore more the capabilities of Pandas.

While Numpy is used for numerical computations Pandas strength lies in data handling and analysis, which makes it the goto package in Data Science.  

### Reading writing files with Pandas

Pandas reads tables of data into a pandas `DataFrames`.

```python
import pandas as pd
!wget https://raw.githubusercontent.com/jbestenlehner/mat1820_example/refs/heads/main/data/bio_stats.csv

df = pd.read_csv('bio_stats.csv') # reads in a CSV file

print(df)                         # displays the content of DataFrame. 
```
For large datasets only the first 5 and last 5 rows are shown while first and last few columns are displayed depending on screen width.

Note: there is an additional 'index' column counting from 0.

If you want to read in only specific columns, there can be indicated with `usecols` similar to `np.loadtxt()`. You can also read in text files separated with whitespaces with `pd.read_csv()`, but this needs to be declared with the parameter `delim_whitespace = True`. For complete list of optional parameters either use `pd.read_csv?` (short help) or `help(pd.read_csv)` (long help).

```python
print(df.columns)   # displays columns name
print(df.dtypes)    # displays columns data types
print(df.shape)     # displays number of rows and columns

df.to_csv('bio_stats_out.csv', index=False) # writes data into CSV excluding the index column
```

By default `index=True` and the index column will be written out as well. An overview of available file formats can be found <a href="https://pandas.pydata.org/docs/user_guide/io.html" target="_blank">here</a>.

### Pandas examples

Below we show a few examples to briefly look at the data with some basics statistics. As you might have noticed the 'bio_stats.csv' file contains height and weight data in SI units (m and kg).

Accessing, selecting subsets and sorting columns of a `DataFrame`:

```python
df = pd.read_csv('bio_stats.csv') # reads in a CSV file
print(df['Age'])                  # accesses and displays the Age column
print(df[['Name', 'Sex']])        # accesses and displays Name and Sex (list of column labels)
print(df.sort_values(by='Age'))   # sorts the df according there Age
print(df['Name'].sort_index(ascending=False)) # sorts Names in descending index order.
```

Similar to numpy `mean()`, `median()` and `std()` are available in Pandas, too.

```python
print(df['Age'].median())              # median value
print(df[['Height', 'Weight']].std())  # standard deviation for Height and Weight
print(df.describe())                   # Calculates, mean(), std(), min(), max() and percentiles boundaries of columns with numerical values.
# You can also group your data and calculate some statistic
print(df.groupby('Sex')['Weight'].mean()) # Mean for female and male
print(df.groupby('Sex').describe())    # Calculates statistics for all numerical columns
print(df.groupby('Sex').describe().T)  # results displayed vertically instead of horizontally
```
You can extract columns from your Pandas `DataFrame` and convert them to numpy arrays.

```python
array_1D = df['Age'].to_numpy() # extracts Age and converts it to a numpy array.
array_2D = df[['Height', 'Weight']].to_numpy() 
```

Filtering data can be done with boolean operators.

```python
print(df['Age'] > 35)        # prints a boolean array.
above35 = df[df['Age'] > 35] # selects rows with Age > 35.
```