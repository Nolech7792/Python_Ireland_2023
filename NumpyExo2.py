import os
import numpy as np

#Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15.#

vect = np.linspace(0,20,21)
for i in range(9,16,1):
    vect[i] = -vect[i]
print(vect)

#Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last.

vect = np.linspace(15,55,41)
for i in range(len(vect)-2):
    print(vect[i+1])

#Write a NumPy program to create a 3X4 array and iterate over it.

mat = np.zeros((3,4))
print(mat)

#Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50.

vect = np.linspace(5,50,10)
print(vect)

#Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10.

vect = np.linspace(0,10,5, dtype = int)
print(vect)

#Write a NumPy program to multiply the values of two given vectors.

def multVect(v1,v2):
    mult = 0
    if len(v1) == len(v2):
        for i in range(len(v1)):
            mult += v1[i]*v2[i]
    print(mult)
multVect([2,4,7,1], [2,9,0,6])

#Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.
mat = np.zeros((3,4))
count = 10
for i in range(3):
    for j in range(4):
        mat[i,j] = count
        count += 1
print(mat)

#Write a NumPy program to find the number of rows and columns in a given matrix.

def nbrRowColumns(mat):
    print(f"Row = {len(mat[0])}")
    print(f"Columns = {len(mat)}")
nbrRowColumns(mat)
    
#Write a NumPy program to create a 4x4 matrix in which 0 and 1 are staggered, with zeros on the main diagonal.
mat = np.identity(4)
print(mat)

"""Write a NumPy program to find common values between two arrays.
Expected Output:
Array1: [ 0 10 20 40 60]
Array2: [10, 30, 40]
Common values between two arrays:
[10 40]"""

def commonValues(ar1,ar2):
    vect = []
    for elem1 in ar1:
        for elem2 in ar2:
            if elem1 == elem2:
                vect.append(elem1)
    print(vect)
commonValues([0,10,20,40,60], [10, 30, 40])

"""Write a NumPy program to get the unique elements of an array.
Expected Output:
Original array:
[10 10 20 20 30 30]
Unique elements of the above array:
[10 20 30]
Original array:
[[1 1]
[2 3]]
Unique elements of the above array:
[1 2 3]"""


def uniqueElem(ar1):
    vect = []
    test = True
    for i in range(len(ar1)):
        for elem in ar1[i]:
            for unique in vect:
                if elem == unique:
                    test = False
            if test == True:
                vect.append(elem)
            test = True
    print(vect)
    

a = np.array([[1, 1],[2, 3]])
uniqueElem(a)
b = np.array([[10,10,20,20,30,30]])
uniqueElem(b)

    

#Write a NumPy program to compute the cross product of two given vectors.

def crossProduct(v1,v2):
    v3 = [v1[1]*v2[2]-v2[1]*v1[2] , v1[2]*v2[0]-v2[2]*v1[0] , v1[0]*v2[1]-v2[0]*v1[1]]
    print(v3)
crossProduct([1,2,3], [4,5,6])   


"""Write a NumPy program to convert cartesian coordinates to polar coordinates of a random 10x2 matrix representing cartesian coordinates.
Expected Output:
[ 0.89225122 0.68774813 0.20392039 1.22093243 1.24435921 1.00358852
0.37378547 0.8534585 0.31999648 0.567451 ]
[ 1.02751197 1.26964967 0.02567519 0.85386412 0.73152767 0.45822494
1.50634505 1.47389983 0.80818521 0.33001182]"""


def cartesianToPolar(mat):
    polar = []
    for i in range(len(mat)):
        r = np.sqrt(mat[i][0] + mat[i][1])
        teta = np.arctan2(mat[i][0],mat[i][1])
        polar.append([r,teta])
    print(polar)
cartesianToPolar([[1,2],[3,4],[5,6]])



"""Write a NumPy program to find the closest value (to a given scalar) in an array.
Original array:
[ 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49
50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74
75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99]
Value to compare:
34.99062268928913
35
"""


def closestValue(og , compare):
    index = 0
    diff = np.abs(og[0] - compare)
    for i in range(len(og)):
        if np.abs(og[i] - compare) < diff:
            diff = np.abs(og[i] - compare)
            index = i
    print(f"Original array: \n{og}")
    print(f"Value to compare: \n{compare}\nClosest value: {og[index]}")
        
closestValue([ 0,1 ,2, 3 ,4 ,5 ,6 ,7 ,8, 9 ,10 ,11, 12 ,13, 14, 15, 16, 17, 18, 19 ,20, 21, 22, 23, 24,
25, 26, 27, 28, 29 ,30, 31, 32, 33 ,34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
, 34.99062268928913)


