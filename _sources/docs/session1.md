# Performing Calculations with Computers

## Learning Objectives:

* To understand why using computers to performing calculations and analysis.
* To become familiar with Colab and Python.
* To be able to apply computing skills to solve Material Science related problems.

## Overview

As material scientists it is important that we are able to use appropriate computing tools in our work. Computers are good in efficiently analysing data, visualising information by creating plots or controlling equipment in the lab. Of course, humans are able to do the same Tasks with pen, paper and a calculator, but challenges will arise:

* **Humans make mistakes:** e.g. swap a digit (*75683424* or *75684324*), accidentally miss a minus sign or make typos in the formula while calculating, e.g. wrongly placed brackets or incorrect units in variable.
* **Humans are slow:** calculating 1000 data points of a formula to draw a graph is not difficult, but will take a long time.
* **Humans are quickly bored with laborious and repetitive Tasks and lose concentration:** How would you feel, if you notice an error in your formula after looking at your graph?

In contrast, computers are good at numerical Tasks and do not make accidentally mistakes, are able to perform certain Tasks in a fraction of a time, and do not complain about laborious and repetitive Tasks.

Computer code is a set of instructions, or a system of rules, written in a specific programming language (e.g. python, C++, java, Assembly language, ...) that tells a computer how to perform specific Tasks. Computers are not inherently intelligent and cannot interpret or guess, what you might mean. They only do what to tell them to do. Artificial intelligence might be able to do this to some extent, but the main purpose of this course is to learn the transferable skills, which can be then applied to many other problems either in Materials Science or any other problem in real life.

## Lecture notes/slides

Lecture notes/slides for all the sessions can be found on <a href="https://vle.shef.ac.uk/ultra/" target="_blank">Blackboard</a>.

## What we are going to cover?

In this course we learn how to use **python**. Python is known for its readability and ease of use. It is a scripting language and follows instruction from the top to bottom and does not need to be compiled before execution like C/C++, Fortran, etc..

* Jupyter notebooks used as interactive scripts on Colab
    * Simple arithmetic
    * Matrices and Operations
    * Plotting
    * Loops and conditional statements
    * Functions and logics
    * Numerical methods
* No prior knowledge or previous computer programming experience is required or assumed.

## Suggested Approach

1. What is the problem?
2. What are your inputs and what are your outputs?
3. Break down the problem into small steps/instructions, e.g. read in data, access the data, ...
4. Work out some key solutions by hand.
5. Develop a Python solution by implementing the list of instructions.
6. Test and debug your Python solution. Nobody writes perfect code on first try.
7. Learn to understand error messages and how to use the help function. 


<!---

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
-->