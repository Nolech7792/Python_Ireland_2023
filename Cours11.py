# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 09:18:29 2023

@author: poiss
"""
import numpy as np




def createVector():
    nel = int(input("Enter the number of elements in the vector: "))
    lvec = [] #we create an emptu list
    for i in range(nel):
        comp = input(f"Enter the value of component {i}")
        lvec.append(float(comp))
    vec = np.array(lvec)
    print(vec)

def createVector2():
    nel = int(input('Enter number elements in the vector : '))
    vec = np.zeros(nel)
    for i in range (nel):
        comp=input(f'Enter the value of component {i} : ')
        vec[i]=float(comp)#we convert it to real and assign it to the 'i  component of vec
        print(vec)
        
def createVector3():
    lin = input("Enter the components of a vector in a line: ")
    smooth = lin.split()
    vec = np.float(smooth)
    print(f"List: {smooth}")
    print(f"Vector: {vec}")
 
def createMat():
    mat=np.zeros((4,3))
    for i in range(4):
        for j in range (3):
            mat[i,j]=float(input(f'Value of element ({i},{j}) : '))
    print(mat)
    

a = np.array([[1,1],[1,2]])
b = np.array([[4,1],[3,1]])
c = np.array([[24,7],[31,9]])
invA = np.linalg.inv(a)
invB = np.linalg.inv(b)
X = np.matmul(invA,c)
X = np.matmul(X,invB)
print(X)

def phExo():
    h = np.array([2.07*10**-5,2.62*10**-7,3.22*10**-5,2.59*10**-4,4.87*10**-5,1.19*10**-4,3.95*10**-5])
    vectPH = -1*np.log10(h)
    print(vectPH)
phExo()



def exo1():
    angtroms = np.linspace(1.0,5.0,21)
    nm = 0.1*angtroms
    print(nm)
#exo1()

def exo2():
    x0 = float(input("Enter the value of x0: "))
    s = float(input("Enter the value of s: "))
    initialx = float(input("Enter the initial value of x: "))
    finalx = float(input("Enter the final value of x: "))
    nbr = int(input("Enter the number of points the table should have: "))
    xVal = np.linspace(initialx, finalx,nbr)
    y = np.exp(-(xVal-x0)**2/(2*(s**2)))/np.sqrt(2*np.pi)   
    print("  x       y")
    for i in range(nbr):
        print(f"{round(xVal[i],3)}   {round(y[i],5)}")
#exo2()
        
def exo3():
    temp_mar = [13.8, 13.3, 13.9, 15.0, 16.4, 20.0, 21.9, 22.3, 22.0, 21.2, 18.8, 16.0]
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December']
    temp_mar_vect = np.array(temp_mar)
    months_vect = np.array(months)
    print(f"Average temperature: {round(np.average(temp_mar_vect),1)}°C")
    min = temp_mar_vect[0]
    min_index = 0
    max = temp_mar_vect[0]
    max_index = 0
    for i in range(len(temp_mar_vect)):
        if temp_mar_vect[i]< min:
            min_index = i
            min = temp_mar_vect[i]
        if temp_mar_vect[i] > max:
            max_index = i
            max = temp_mar_vect[i]
    print(f"Min temperarture: {min}°C, {months_vect[min_index]}")
    print(f"Max temperature: {max}°C, {months_vect[max_index]}")
    
#exo3()

def exo4():
    nbrStudents = int(input("Enter the number of students who have taken the test: "))
    theoryExam = []
    problemExam = []
    for i in range(nbrStudents):
        theoryExam.append(float(input(f"Enter the grade of the students n°{i+1} for the theory exam: ")))
        problemExam.append(float(input(f"Enter the grade of the students n°{i+1} for the theory exam: ")))
    theoryVect = np.array(theoryExam)
    problemVect = np.array(problemExam)
    print("n° of student  Theory exam   Problem exam   Total grade")
    max = 0 
    index_max = 0 
    min = 10 
    avg = 0
    index_min = 0
    for i in range(nbrStudents):
        print(f"{i+1}                 {theoryVect[i]}         {problemVect[i]}         {round(theoryVect[i]*0.40 + problemVect[i]*0.60,2)}")
        avg = avg + theoryVect[i]*0.40 + problemVect[i]*0.60
        if theoryVect[i]*0.40 + problemVect[i]*0.60 < min :
            min = theoryVect[i]*0.40 + problemVect[i]*0.60
            index_min = i
        if theoryVect[i]*0.40 + problemVect[i]*0.60 > max:
            max = theoryVect[i]*0.40 + problemVect[i]*0.60
            index_max = i
    print(f"Max total grade = {round(max,2)}. Student n°{index_max}")
    print(f"Min total grade = {round(min,2)}. Student n°{index_min}")
    print(f"The Average is: {round(avg/nbrStudents,2)}")
#exo4()

