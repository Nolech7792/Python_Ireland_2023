import math as m

R = 0.08206
n = 0.5
T = 298.15
V = 2.5
P = n*R*T/V
print("At temperature {} K the pressure is {} atm.".format(T,P))

#commentaire simple 

"""commentaire
avec début
et 
fin"""

def enterName(n):
    name = input("Enter your name: ")
    print("your name is: {}.".format(name))

def enterNumber(n):
    number = int(input("Enter a number: ")) #error if input not a int#
    print("your number is: {}.".format(number))

def volume(r,h):
    V = (1/3)*m.pi*(r**2)*h
    print("The volume for a sphere with r = {} and h = {} is: {}.".format(r,h,V))

volume(10,3)
volume(10,5)
volume(15,2)
volume(12,5)