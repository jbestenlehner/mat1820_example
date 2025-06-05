# Plotting graphs and visualising data

## Learning Objectives:

* Plotting graphs and figures.
* Visualisation of data.
* Line, symbols and bar graph plus histograms.

## Overview

### Graphs for scientific use:

Graphs are the best way of showing data! Looking at tables with numbers doesn't show you much. However, any data shown in plots, graphs or figures should be made available, e.g. appendix, online, database, ...  

**Data points:** 
* Should be clearly visible (shows where you have data, and where you don’t!)
* Should not join up data points (makes noise look like a trend!)
* Fitted trend lines must reproduce the shape of the data (don’t force linearity!) 

**Axes:**
* Must have labels (Unlabelled data has **no** meaning!)
* Must have units (Show how strong correlations between variables are!)

**Scale:** 
* The data of interest **must** be clear to see (otherwise, what’s the point?!?)

**Captions:** 
* Tell the reader what they are looking at (not their job to work it out!)


### Figures in reports, publications, thesis, books, ...:

**Always ask:**
1. What is the point of this figure?
    * Does it contribute to the story you are telling the reader?
2. Is it illustrating the point you are trying to make?
    * If not, you’ve plotted the wrong thing!
3. Is it clear?
    * If not, how can you help the reader understand what it shows.

To help the reader you can:
* **Annotate** – add some arrows, boxes or text on the figure to help show the reader the important parts of the data?
* **Remove Distractions** – Avoid visual clutter that isn’t relevant.
* **Exploit the Caption** – Describe what you are showing. Make sure key input data is stated.

### Analysis and discussion of data

**Data analysis, post-processing and studying data with the aim of:**
1. Extracting useful information (e.g. trends, correlations, magnitudes of effects).
2. Informing conclusions.
3. Supporting decision-making.

**Data analysis should:**
* Draw key values, trends and relationships out from your data.
    * Make sure you quote important numerical values directly! Be quantitative!
* Relate these to the science of the system.
* Where appropriate/possible, compare or contrast with the literature and/or other ways of obtaining data.
* Reflect on your actual data and observations.
    * Don’t project conclusions you can’t back up!
* Explore the accuracy and limitations of your work.
    * No study is perfect

## Plotting and visualising data with Python

The plotting library in Python is called [_matplotlib_](https://matplotlib.org/stable/). It can be used for creating plots, animated figures, and interactive visualisations. Some examples with example program code are shown [here](https://matplotlib.org/stable/gallery/index.html).

In this session we will use the [_pyplot_](https://matplotlib.org/stable/api/pyplot_summary.html) module from the _matplotlib_ library. The module is imported with:

```python
import matplotlib.pyplot as plt
```

The function for plotting is called [_plt.plot()_](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html). An example could look like this

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1) # generates an array from 0 to 5 in 0.1 steps
y = np.sin(x)            # calculates the sin of the x array
plt.plot(x, y)           # plots the dependent variable y against the independent variable x.
plt.show()               # shows the plot
```
To improve your plot you could chose a different colour, line style or using markers (symbols) instead of lines. _pyplot_ has predefined colours, line styles and markers, which can be used without using _keywords_ like `color`, `linestyle` or `marker`.

```python
plt.plot(x, y, 'ro')  # plot data as red circles
plt.plot(x, y, 'm--') # joins point with magenta dashed line. 
```

### Table of base colours:

|colour | description|
|:-----|:-------|
| 'b' | blue    |
| 'g' | green   |
| 'r' | red     |
| 'c' | cyan    |
| 'm' | magenta |
| 'y' | yellow  |
| 'k' | black   |
| 'w' | white   |

A list of colour names is shown [here](https://matplotlib.org/stable/gallery/color/named_colors.html).

### Table of line styles:

| line style | description|
|:-----|:-------|
| '-'  | solid line |
| '--' | dashed line |
| '-.' | dash-dot line |
| ':'  | dotted line |

A list of line styles is shown [here](https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html).

### Table of markers or plot symbols:

| marker | description |
|:-----|:-------|
|'.' | point |
|'o' | circle|
|'v' | triangle_down|
|'^' | triangle_up|
|'<' | triangle_left|
|'>' | triangle_right|
|'s' | square|
|'D' | diamond|
|'d' | thin diamond|
|'*' | star|

A list of markers is shown [here](https://matplotlib.org/stable/api/markers_api.html).