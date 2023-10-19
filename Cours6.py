#LIST#
def coursList():
    names = ["Sam","Chris","Bob","Colette"] #list = [,,,,]
    print(names)
    print(names[2])
    names.append("Nash") #add
    print(names)
    names.remove("Sam") 
    print(names)
    names.remove(names[0])
    print(names)
    names[0] = "Michelle" #update
    print(names)
    for i in names :
        print(i)
#coursList()

#TUPLE# #(pas modifiable)#
def coursTuple():
    voyelles = ("a","e","i","o","u","y")
    for i in voyelles:
        print(i)
#coursTuple()

#set# {}

def exemplesList():
    smooth = [3.14,7,-2 + 3j, 'water', False, [1,2]]
    print(smooth[1:3])
    print(smooth[:4])
    smooth = smooth + [5,"Hello","Hi",'7',"e"]
    print(smooth[::2])
    print(smooth)

    print(smooth[-1])
    print(smooth[-2])
    print(smooth[-4:-2])
#exemplesList()

#Exercices#

def creeListNumero():
    nbrNumeros = int(input("Enter the number of numbers"))
    listNum = []
    for i in range(nbrNumeros):
        val = int(input("Enter a value"))
        listNum.append(val)
    print(listNum)
#creeListNumero()

def exempleSplit(): #cree une list de valeurs
    line = input("Enter a serie of numbers separated by a space : ")
    numbersStr = line.split()
    print(numbersStr)
    numbersFloat = []
    for elem in numbersStr:
        numbersFloat.append(float(elem))
    print(f"Your list is : {numbersFloat}")
#exempleSplit()

def listnFirstNaturalNumber(n):
    listNaturalNumbers = list(range(n))
    print(f"The list is {listNaturalNumbers}")

#listnFirstNaturalNumber(12)
    
def gradesStudents():
    grades = []
    names = []
    name = "name"
    while name != "":
        name = input("\nEnter your name (enter nothing if you are done) : ")
        if name != "":
            grade = int(input(f"Hi {name}.\nEnter your grade : "))
            names.append(name)
            grades.append(grade)
    print("\nHere are the grades of all the students:\n")
    average = 0
    for i in range(len(names)):
        print(f"{names[i]} : {grades[i]}")
        average += grades[i]
    average = average/len(names)
    print(f"The average is : {average}")
#gradesStudents()