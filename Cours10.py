# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 09:43:18 2023

@author: poiss
"""

import numpy as np

a = np.array([1,2,3], dtype = 'int32')
print("a = \n" + str(a))

print("a.dim = \n" + str(a.ndim))


b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print("b = \n" + str(b))

print("b.dim = " + str(b.ndim))
print("b.shape = " + str(b.shape))

print("a.dtype = " + str(a.dtype))
print("b.dtype = " + str(b.dtype))

print("a.itemsize = " + str(a.itemsize))
print("a.size = " + str(a.size))
print("a.nbytes = " + str(a.nbytes))

print("b.size = \n" + str(b.size))

print("b = \n" + str(b))

print("b[1,1] = \n" + str(b[1,1]))

print("b[:,1] = \n" + str(b[:,1]))

c = np.array([[1,2,3,4,5,6,7],
              [8,9,10,11,12,13,14]])
print("c =\n" +str(c) )
print("c[1,0:-1:2] = " + str(c[1,0:-1:2]))
print("c[1,0: :2] = " + str(c[1,0: :2]))
print("c[0: :2] = " + str(c[:,0: :2]))

zero = np.zeros((4,5))
print("zero = \n" + str(zero))

one = np.ones((4,5))
print("one = \n" + str(one))

ident = np.identity(5)
print("ident = \n" + str(ident))


arr= np.array([[1,2,3]])
r1 = np.repeat(arr,3, axis = 0)
print ("r1 = \n" + str(r1))


mat = np.ones((5,5))
z = np.zeros((3,3))
z[1,1] = 9
mat[1:-1,1:-1] = z

print("mat = \n" + str(mat))



a1 = np.array([1,2,3])
a2 = a1
a2[0] = 10
print("using a2 = a1")
print("a2 = " + str(a2))
print("a1 = " + str(a1))

a3 = np.array([1,2,3])
a4 = np.copy(a3)
a4[0] = 10
print("using a4 gv= np.copy(a3)")
print("a4 = " + str(a4))
print("a3 = " + str(a3))



calcul = np.array([[1,2,3,4],[5,6,7,8]])
print("calcul = \n " + str(calcul))
print("calcul + 2 =\n" + str(calcul +2))
print("calcul * 2 =\n" + str(calcul *2))
print("calcul ** 2 =\n" + str(calcul **2))

multi = np.array([[1,2],[3,4],[5,6],[7,8]])
print("multi = \n" +str(multi))
print("np.matmul(calcul,multi) = \n" + str(np.matmul(calcul,multi)))



rand = np.random.randint(-10,10,size = (5,7))
print("rand = \n" + str(rand))
print("min = " + str(np.min(rand)))
print("min axis 0(row) = " + str(np.min(rand, axis = 0)))
print("min axis 1(column) = " + str(np.min(rand, axis = 1)))
print("returns the row or column that has all the minimum number per row or column")



print("rand sum = " + str(np.sum(rand)))
print("rand axis 0 (row) sum = " + str(np.sum(rand, axis = 0)))
print("rand axis 1 (column) sum = " + str(np.sum(rand, axis = 1)))



npoints = 21
values = np.linspace(-2.0,2.0,npoints)
print(f"values = {values}")

#vect = np.linspace(10,30,21,dtype = 'int32')
vect = np.arange(10,31)
vect[4] = 1
print(vect)
