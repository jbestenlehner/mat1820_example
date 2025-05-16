# Vectors and Matrices

## Learning Objectives:

* Creating and indexing vectors and matrices.
* Mathematical operations on vectors and matrices.
* Application in Material Science.

## Overview

A **scalar** is described by a single pure number. It has zero dimension or is of rank 0. 

A **vector** is a term that refers to quantities that cannot be expressed by a single number (a scalar), or to elements of some vector spaces. They have to be expressed by both magnitude (or length) and direction. For example the application of a force to an object can be described by a vector, which indicates the direction of the applied force and its magnitude (length of vector). A vector has one dimension and is of rank 1.

A **matrix** is a rectangular array or table of numbers, e.g. data, with elements or entries arranged in <span style="color:blue">**m-rows**</span> (horizontal) and  <span style="color:red">**n-columns**</span> (vertical): 


```{math}
\begin{bmatrix}
a_{\textcolor{blue}{1}\textcolor{red}{1}} & a_{\textcolor{blue}{1}\textcolor{red}{2}} & \ldots & a_{\textcolor{blue}{1}\textcolor{red}{n}} \\
a_{\textcolor{blue}{2}\textcolor{red}{1}} & a_{\textcolor{blue}{2}\textcolor{red}{2}} & \ldots & a_{\textcolor{blue}{2}\textcolor{red}{n}} \\
a_{\textcolor{blue}{3}\textcolor{red}{1}} & a_{\textcolor{blue}{3}\textcolor{red}{2}} & \ldots & a_{\textcolor{blue}{3}\textcolor{red}{n}} \\
\vdots & \vdots & \ddots & \vdots \\
a_{\textcolor{blue}{m}\textcolor{red}{1}} & a_{\textcolor{blue}{m}\textcolor{red}{2}} & \ldots & a_{\textcolor{blue}{m}\textcolor{red}{n}} \\
\end{bmatrix}
.
```
The matrix is of dimension $m\times n$. The rank of the matrix $ \leq n$, if $n < m$, or $ \leq m$, if $m < n$. See also your math lectures.

Further reading including Python example on how scalars, vectors, matrices and tensors relate to each other can be found [here](https://www.kdnuggets.com/2018/05/wtf-tensor.html).

## Matrix operations

### Addition

The sum **$A + B$** of two m×n matrices **$A$** and **$B$** is calculated entrywise:

```{math}
\begin{bmatrix}
1 & 2 & 1\\
3 & 4 & 3\\
\end{bmatrix}
+
\begin{bmatrix}
5 & 6 & 5\\
7 & 8 & 7\\
\end{bmatrix}
=
\begin{bmatrix}
1+5 & 2+6 & 1+5\\
3+7 & 4+8 & 3+7\\
\end{bmatrix}
=
\begin{bmatrix}
6 & 8 & 6\\
10 & 12& 10\\
\end{bmatrix}
```

### Scalar multiplication

The product **$cA$** of a number $c$ (also called a scalar in this context) and a matrix **$A$** is computed by multiplying every entry of **$A$** by $c$:

```{math}
3 \cdot
\begin{bmatrix}
1 & 2 & 1\\
3 & 4 & 3\\
\end{bmatrix}
=
\begin{bmatrix}
3\cdot 1 & 3\cdot 2 & 3\cdot 1\\
3\cdot 3 & 3\cdot 4 & 3\cdot 3\\
\end{bmatrix}
=
\begin{bmatrix}
3 & 6 & 3\\
9 & 12& 9\\
\end{bmatrix}
```

### Matrix multiplication

Multiplication of two matrices $A$ and $B$ is given by the [dot product](#dot-product-of-2-vectors) of the corresponding row of $A$ and the corresponding column of $B$ (row times column):

```{math}
\begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6\\
\end{bmatrix}
\begin{bmatrix}
1 & 2\\
3 & 4\\
5 & 6\\
\end{bmatrix}
=
\begin{bmatrix}
1\cdot1+2\cdot3+3\cdot5 & 1\cdot2+2\cdot4+3\cdot6\\
4\cdot1 + 5\cdot3 + 6\cdot5 & 4\cdot2 + 5\cdot4 + 6\cdot6\\
\end{bmatrix}
=
\begin{bmatrix}
22 & 28\\
49 & 64\\
\end{bmatrix}
```

Note: matrix multiplications are not commutative.

### Transposition

The transpose of an $m\times n$ matrix $A$ is the $n\times m$ matrix $A^{\mathrm{T}}$ formed by turning rows into columns and vice versa: 

```{math}
\begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6\\
\end{bmatrix}^{\mathrm{T}}
=
\begin{bmatrix}
1 & 4\\
2 & 5\\
3 & 6\\
\end{bmatrix}
```

### Dot product of 2 vectors

The dot product of vectors $\vec{a}$ and $\vec{b}$ is given by

```{math}
\vec{a} \cdot \vec{b} = \sum_{i=1}^n a_i b_i = a_1 b_1 + a_2 b_2 + \ldots + a_n b_n.
```