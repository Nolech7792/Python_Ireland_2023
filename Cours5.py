def factoriel():
    n = int(input("Enter a positive integer : "))
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print(f"{n}! = {fact}")

def factorielRecursif(n, fact = 1, i = 1):
    if i > n :
        print(f"{n}! = {fact}")
    else:
        factorielRecursif(n, fact*i, i+1)

#factoriel()

#n = 5
#factorielRecursif(n)

def exoBiz():
    for i in range(1000):
        a = i % 10
        b = (i % 100)//10
        c = (i%1000)//100
        rep = a**3 + b**3 + c**3
        if i == rep:
            print(f"{i} = {c}**3 + {b}**3 + {a}**3")

#exoBiz()

def isPrime():
    num = int(input("Enter a positive inter : "))
    test = True
    for i in range(2,num):
        if num % i == 0:
            test = False
            #print(f"{num} is not a primary number")
            #break
    if test == False:
        print(f"{num} is not a primary number")
    else:
        print(f"{num} is a primary number")

#isPrime()

