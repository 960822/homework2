Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 12:54:16) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> def matrixMul(A,B):
	res = [[0]*len(B[0]) for i in range(len(A))]
	for i in range(len(A)):
		for j in range(len(B[0])):
			for k in range(len(B)):
				res[i][j]+=A[i][k]*B[k][j]
	return res

>>> a=[[1,2,3],[4,5,6],[7,8,9]]
>>> b=[[1,2,3],[4,5,6],[7,8,9]]
>>> print matrixMul(a,b)
[[30, 36, 42], [66, 81, 96], [102, 126, 150]]
>>> 
>>> def matrixMul2(A,B):
	return[[sum(a*b for a,b in zip(a,b))for b in zip(*B)]for a in A]

>>> a=[[1,2,3],[4,5,6],[7,8,9]]
>>> b=[[1,2,3],[4,5,6],[7,8,9]]
>>> print matrixMul2(a,b)
[[30, 36, 42], [66, 81, 96], [102, 126, 150]]
>>> 
>>> import numpy as ny
>>> a=ny.array([[1,2,3],
	        [4,5,6],
	        [7,8,9]])
>>> b=ny.array([[1,2,3],
	        [4,5,6],
	        [7,8,9]])
>>> ny.dot(a,b)
array([[ 30,  36,  42],
       [ 66,  81,  96],
       [102, 126, 150]])
>>> ny.dot(b,a)
array([[ 30,  36,  42],
       [ 66,  81,  96],
       [102, 126, 150]])
>>> 
