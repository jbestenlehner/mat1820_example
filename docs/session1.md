# Performing Calculations with Computers

## Learning Objectives:

* To understand why using computers to performing calculations and analysis.
* To become familiar with Colab and Python.
* To be able to apply computing skills to solve Material Science related problems.

## Overview

As material scientists it is important that we are able to use appropriate computing tools in our work. Computers are good in efficiently analysing data, visualising information by creating plots or controlling equipment in the lab.Of course, humans are able to do the same tasks with pen, paper and a calculator, but challenges will arise:

* **Humans make mistakes:** e.g. swap a digit (*75683424* or *75684324*), accidentally miss a minus sign or make typos in the formula while calculating, e.g. wrongly placed brackets or incorrect units in variable.
* **Humans are slow:** calculating 1000 data points of a formula to draw a graph is not difficult, but will take a long time.
* **Humans are quickly bored with laborious and repetitive tasks and lose concentration:** How would you feel, if you notice an error in your formula after looking at your graph?

In contrast, computers are good at numerical tasks and do not make accidently mistakes, are able to perform certain tasks in a fraction of a time, and do not complain about laborious and repetitive tasks.

## Lecture notes

Lecture notes for session 1 can be found [here](https://vle.shef.ac.uk/bbcswebdav/pid-6851883-dt-content-rid-51025017_1/xid-51025017_1).

## Some examples

For the measurement noise $n^{(i)}$ of the $i$-th observation we use the error-spectrum from the data reduction which is assumed for simplicity to be Gaussian with zero mean and signal independent,
```{math}
:label: eqgnm
\begin{eqnarray}\label{eq:gnm}
\mathcal{P}(n^{(i)}|s^{(i)}) & = & \mathcal{G}(n^{(i)},N^{(i)})\\
 & = & \frac{1}{\sqrt{|2\pi N^{(i)}|}}\exp\left[-\frac{1}{2}n^{(i)\dagger}\left(N^{(i)}\right)^{-1}n^{(i)}\right]\nonumber 
\end{eqnarray}
```
with assumed noise covariance $N^{(i)}=\langle n^{(i)}n^{(i)\dagger}\rangle_{(n^{(i)}|s^{(i)})}$. More details on equation {eq}`eqgnm` can be found in {cite}`bestenlehner2024`.

```{bibliography}
```
