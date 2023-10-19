# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:01:54 2023

@author: poiss
"""

import os
import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline

x = np.linspace(-2,2,101)
y = x**2
print(x)

plt.plot(x,y)
plt.title("Graph of x^2 vs x")
plt.xlim(-1.5,1.5)
plt.ylim(0,3)
plt.show()



x = np.linspace(0,3*np.pi, 500)

plt.plot(x, np.sin(x**2))
plt.title('A simple chirp')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

x = np.linspace(-2,2,101)
plt.xlabel("x")
plt.ylabel("f(x)")
y = x**2
plt.plot(x,y, 'g', label = "x^2",)
y2 = x**4
plt.plot(x,y2, 'ro', label = "x^4")
plt.legend()
#plt.savefig("fig1.png")
plt.show()


def fctCos():
    n = int(input("enter the number of points you want : "))
    x = np.linspace(-1,1,n)
    y =np.cos(2*np.pi*x)
    plt.plot(x,y, 'o')
    plt.title("2 pi x")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.savefig("cos2pix.png")
    plt.show()
    
#fctCos()

def fctCosSin():
    n = int(input("enter the number of points you want : "))
    x = np.linspace(-1,1,n)
    y = np.cos(2*np.pi*x)
    y2 = np.sin(2*np.pi*x)
    plt.plot(x,y, 'bo', label = "cos(2*pi*x)")
    plt.plot(x,y2,'yo', label = "sin(2*pi*x)")
    plt.title("cos() and sin() 2 pi x")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.savefig("CosSin2pix.png")
    plt.show()
#fctCosSin()


def fctGraph():
    test = False
    while test == False:
        n = input("enter the number of points you want : ")
        try:
            int(n)
        except:
            print("Enter a valid integer!\n")
        else:
            test = True   
            n = int(n)
    x = np.linspace(0,4,n)
    y =np.sin(np.pi*x)*np.sin(20*np.pi*x)*np.exp(-x)
    plt.plot(x,y, 'bo')
    plt.plot(x,y,'r')
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()
#fctGraph()

def fctGas():
    test = False
    while test == False:
        n = input("enter the number of points you want : ")
        try:
            int(n)
        except:
            print("Enter a valid integer!\n")
        else:
            test = True   
            n = int(n)
    test = False
    while test == False:
        T = input("enter the temperature : ")
        try:
            float(T)
        except:
            print("Enter a valid float!\n")
        else:
            test = True   
            T = float(T)
    Vm = np.linspace(2,10,n)
    y = 0.08206*T/Vm
    plt.plot(Vm,y, 'o')
    plt.title("Isotherm (ideal gas)")
    plt.xlabel('L/mol')
    plt.ylabel('pa')
    plt.savefig("isotherm.jpg")
    plt.show()
#fctGas()

def fctGasLoop():
    test = False
    while test == False:
        n = input("enter the number of points you want : ")
        try:
            int(n)
        except:
            print("Enter a valid integer!\n")
        else:
            test = True   
            n = int(n)
    test = False
    while test == False:
        nbr = input("enter the number of temperatures you want : ")
        try:
            int(nbr)
        except:
            print("Enter a valid integer!\n")
        else:
            test = True   
            nbr = int(nbr)
    
    T = []
    for i in range(nbr): 
        test = False
        while test == False:
            Temp = input(f"enter the temperature {i+1}: ")
            try:
                float(Temp)
            except:
                print("Enter a valid float!\n")
            else:
                test = True   
                T.append(float(Temp))
    
    for i in range(nbr):
        Vm = np.linspace(2,10,n)
        y = 0.08206*T[i]/Vm
        plt.plot(Vm,y, 'o')
        plt.title("Isotherm (ideal gas)")
        plt.xlabel('L/mol')
        plt.ylabel('pa')
        plt.show()
#fctGasLoop()

def Gaussianfct():
    test = False
    while test == False:
        n = input("enter the number of points you want : ")
        try:
            int(n)
        except:
            print("Enter a valid integer!\n")
        else:
            test = True   
            n = int(n)
    test = False
    while test == False:
        xdeb = input("Initial value : ")
        try:
            float(xdeb)
        except:
            print("Enter a valid float!\n")
        else:
            test = True   
            xdeb = float(xdeb)
    test = False
    while test == False:
        xfin = input("Final value : ")
        try:
            float(xfin)
        except:
            print("Enter a valid float!\n")
        else:
            test = True   
            xfin = float(xfin)
    x = np.linspace(xdeb,xfin,n)
    y = np.exp(-(x-0)**2/(2*(0.3**2)))/np.sqrt(2*np.pi)
    plt.plot(x,y, 'o')
    plt.title("Gaussian Fonction")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()
#Gaussianfct()

def expSin():
    test = False
    while test == False:
        n = input("enter the number of points you want : ")
        try:
            int(n)
        except:
            print("Enter a valid integer!\n")
        else:
            test = True   
            n = int(n)
    x = np.linspace(0,3,n)
    y = np.exp(-x)
    y2 = np.sin(3*np.pi*x)*np.exp(-x)
    plt.plot(x,y, 'b', label = "e-x")
    plt.plot(x,y2,'orange', label = "sin(3*pi*x)")
    plt.title("Functions")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.show()
#expSin()

def Gaussianfctmultiple():
    test = False
    while test == False:
        n = input("enter the number of points you want : ")
        try:
            int(n)
        except:
            print("Enter a valid integer!\n")
        else:
            test = True   
            n = int(n)
    test = False
    test = False
    while test == False:
        nbr = input("enter the number of graph you want : ")
        try:
            int(nbr)
        except:
            print("Enter a valid integer!\n")
        else:
            test = True   
            nbr = int(nbr)
    for i in range(nbr):
        test = False
        while test == False:
            x0 = input("x0 : ")
            try:
                float(x0)
            except:
                print("Enter a valid float!\n")
            else:
                test = True   
                x0 = float(x0)
        test = False
        while test == False:
            s = input("s : ")
            try:
                float(s)
            except:
                print("Enter a valid float!\n")
            else:
                test = True   
                s = float(s)
        x = np.linspace(-2,2,n)
        y = np.exp(-(x-x0)**2/(2*(s**2)))/np.sqrt(2*np.pi)
        plt.plot(x,y, 'o')
        plt.title("Gaussian Fonction")
        plt.xlabel('x')
        plt.ylabel('f(x)')
    plt.show()
Gaussianfctmultiple()