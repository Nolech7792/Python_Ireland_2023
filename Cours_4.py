def numberDivisible():
    num = int(input("Enter a number : "))
    quotient = 1
    nbrRep = 0
    while quotient < num:
        if num % quotient == 0 :
            print(f"{num} is divisible by {quotient}")           
            nbrRep += 1
        quotient += 1
    print(f"the number {num} has {nbrRep} divisors")
numberDivisible()

name = 'Jessa29roy'
size = len(name)
i = -1
while i < size - 1 :
    i = i + 1
    if not name[i].isalpha():
        continue
    print(name[i], end='')
print('\n')

i = -1
while i < size - 1 :
    i = i + 1
    if name[i].isdecimal():
        break
    print(name[i], end='')
print('\n')