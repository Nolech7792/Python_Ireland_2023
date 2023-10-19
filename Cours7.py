def listOfNumbers():
    nbr = 'Z'
    listNbr = []
    while str(nbr) != '':
        nbr = input("Enter a number (or just press enter to finish) : ")
        if nbr != '':
            listNbr.append(int(nbr))
    print("\nThe numbers you have written are :")
    average = 0.0
    for elem in listNbr:
        print(elem)
        average += elem
    average = average / len(listNbr)
    print(f"The average is : {average}")

#listOfNumbers()

def stringOfNames():
    names = input("Enter a serie of names de perated by a space :\n")
    listNames = names.split()
    print("")
    for elem in listNames:
        print(f"Hi, {elem}")

#stringOfNames()

def molecularMass():
    listElements = ["H","C","N","O","S","Cl"]
    listAtomicMass = [1.008,12.011,14.007,15.999,32.065,35.453]
    element = "zer"
    nbrAtoms = 0
    massMolecule = 0.0
    while element != "":
        element = input("Enter the element : ")
        if element != "":
            nbrAtoms = int(input("Enter the number of atoms : "))
            massMolecule = listAtomicMass[listElements.index(element)]*nbrAtoms
    print(f"The mass of your element is : {massMolecule}")

#molecularMass()

def polynomialFunction():
    listCoef = []
    fct = ""
    n = int(input("Enter the degre of you function : "))
    for i in range(n+1):
        listCoef.append(float(input(f"Enter the coef of x^{i} : ")))   
    for i in range(n+1):
        if listCoef[i] != 0:
            fct += str(listCoef[i]) + f"x^{i} "
    print(f"your function is : {fct}")
    x = float(input("Enter a value for x : "))
    solution = 0
    count = 0
    for i in range(n+1):
        solution += listCoef[i] * (x**i)
    print(f"f({x}) = {solution}")

#polynomialFunction()

def wish(*names):
    return names
names = ['tonton', "tata",2]
print(wish(names))