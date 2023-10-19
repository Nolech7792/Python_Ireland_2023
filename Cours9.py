
def youngest_kid(*kids):
    print("The youngest kid is "+ kids[2])

#youngest_kid("Cole","Emma","James","Stephanie")

def dict_child(**kids):
    print("The favorite kid is " + kids["kid1"])

#dict_child(kid1 = "Cole", kid2 = "Emma", kid3 = "James", kid4 = "Stephanie")

def fctToPassWithoutError():
    pass

fctToPassWithoutError()

def min_max_list():
    listNbr = []
    for i in range(5):
        listNbr.Append(int(input("Enter a number")))
    print(listNbr)
    max = listNbr[0]
    min = listNbr[0]
    for i in listNbr:
        if i < min:
            min  = i
        if i > max:
            max = i
    print(f"The min is {min} and the max is {max}")

#min_max_list()


#### TRY EXCEPT ###

try :
    pass
except Exception:
    pass
except FileNotFoundError:
    pass
else:
    pass
finally:
    pass


def OddOrEven():
    test = False
    while test == False:
        nbr = input("Enter a number : ")
        try:
            int(nbr)
        except Exception:
            print("Enter a valid number!\n")
        else:
            test = True
    if(int(nbr) % 2) == 0:
        print(f"{nbr} is even")
    else:
        print(f"{nbr} is odd")       

OddOrEven()