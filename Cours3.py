import random



message = "good morning"
print(len(message)) #taille de la chaien e caractere#
print(message[1]+message[2]+message[6]) #renvoie la valeur de la n-ieme lettre (indexe de départ 0)#
print(message[0:4]) #renvoie les valeur entre le point de départ(inclu) et l'arrivee(non-inclu)#
print(message[:11]) #dudébut jusqu'au n#
print(message[8:]) #jusqua la fin#
print(message[-1])#lire a l'envers#
print(message.count('g'))#nbr de fois ou le caractere apparait#
print(message.find('o'))#retourne la première psition de la lettre#
print(message.replace('morning','night'))
print(message.replace('d','t'))
print(dir(str)) #retourne toutes les fonctions possible avec un string(idem pour int...)#

def game():
    secretNumber = random.randint(0,20)
    outcome = False
    while outcome == False:
        response = int(input("Try to find the secret number between 0 and 20 included \n"))
        if secretNumber == response: 
            outcome = True
        elif secretNumber > response :
            print("Try a bigger number")
        else :
            print("Try a smaller number")
        print("\n\n")
    print("You WIN! the secret numbrer was {}.".format(secretNumber))
#game()

def BMI() :
    weight = float(input("Please enter you weight (kg) : "))
    height = float(input("Please enter you height (m) : "))
    bmi = weight / (height**2)
    if(bmi < 18.5):
        print("Your BMI is: "+f"{bmi}, You are underweight (dont forget to eat)")
    elif(bmi < 25):
        print("Your BMI is: "+f" {bmi}, You have a normal weight, NICE JOB!")
    elif(bmi < 30):
        print("Your BMI is: "+f" {bmi}, You are overweight, HIT THE GYM NOW!")
    elif(bmi >= 30):
        print("Your BMI is: "+f" {bmi}, You are obese, GET YOURSELF TOGETHER YOU FAT ****!")

#BMI()

def isDivisible():
    n1 = int(input("Enter a first number : "))
    n2 = int(input("Enter a second number : "))
    answer = n1 // n2
    reste = n1 % n2
    if(n1%n2 == 0):
        print(f"{n1} is divisible by {n2} and the division is {n1}/{n2} = {answer}")
    else:
        print(f"{n1} is not divisible by {n2} and the division is {n1}/{n2} = {answer}, remainder {reste}")
isDivisible()

def isSmaller() :
    n1 = int(input("Enter a first number : "))
    n2 = int(input("Enter a second number : "))
    if(n1 < n2):
        print(f"{n1} is smaller")
    elif(n1 = n2):
        print(f"{n2} is smaller")
    else :
        print(f"{n1} = {n2}")