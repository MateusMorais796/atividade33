lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

list1a9 = []
list8a13 = []
numpar = []
numimpar = []
multiplode2 = []
mult3 = []
mult4 = []
listreverse = []
razao = []

for n in lista:
    if n<10 and n>0:
        list1a9.append(n)
    if n>7 and n<14:
        list8a13.append(n)
    if n %2 == 0:
        numpar.append(n)
    if n%2 != 0:
        numimpar.append(n)
lista_rev = list(reversed(lista))

for n in lista:
    if 2*0 == n:
        multiplode2.append(n)
    if 2*1 == n:
        multiplode2.append(n)
    if 2*3 == n:
        multiplode2.append(n)
    if 2*4 == n:
        multiplode2.append(n)
    if 2*5 == n:
        multiplode2.append(n)
    if 2*6 == n:
        multiplode2.append(n)
    if 2*7 == n:
        multiplode2.append(n)
    if 2*8 == n:
        multiplode2.append(n)
    if 3*1 == n:
        mult3.append(n)     
    if 3*2 == n:
        mult3.append(n)
    if 3*3 == n:
        mult3.append(n)
    if 3*4 == n:
        mult3.append(n)
    if 3*5 == n:
        mult3.append(n)
    if 4*1 == n:
        mult4.append(n)    
    if 4*2 == n:
        mult4.append(n)  
    if 4*3 == n:
        mult4.append(n)  

multiplos = [multiplode2, mult3, mult4]
int10a15 = []
int3a9 = []

for n in lista:
    if n>9 and n<16:
        int10a15.append(n)
    if n>2 and n<10:
        int3a9.append(n)

razao = sum(int10a15)/sum(int3a9)
razao2 = [float(razao)]


print(list1a9)
print(list8a13)
print(numpar)
print(numimpar)
print(multiplos)
print(lista_rev)
print(razao2)