import math
import random
# define function on value
def function(x1):
    while True:
        try:
            value = int(input(x1))
        except :
            print("HUEVON")
            continue
        else:
            break
    return int(value)

# define values and validation
while True:

    n2=function("Ceros: ")
    a2=function("Primer valor A: ")
    b2=function("Segundo valor B:")
    c2=function("Iteraciones:")

    if a2<=b2 :
        print("A no puede ser menor que B")
        continue

    if a2<=0 or b2<=0 or n2<1 or c2<1:
        print("Valores negativos no aceptados")
        continue

    else:
        break

#prueba de fuego
a=0
b=0
c=0
n=0
Good=0
Bad=0
for ii in range(1,c2+1):
    while True:
        a=random.randint(1,a2)
        b=random.randint(1,b2)
        if a>b:
            break
        else:
            continue
    n=random.randint(1,n2)
    jota= math.log(a/b,10)
    ka = math.floor(jota)
    if n-ka < 0 :
        enemenoska = 0
    else:
        enemenoska = n-ka
    alfa = math.floor(ka / jota)
    if n/jota>=1:
        beta=1
    else:
        beta=0
    counta=0
    countb=0
    n=int(n)

    for i in range (n+1):
        val1=a*(10**i)
        for j in range(n+1):
            val2=b*(10**j)

            if val1> val2:
                counta = counta+1
            elif val1 < val2:
                countb = countb + 1


    primero= (enemenoska*(enemenoska+1))/2
    segundo1 = (n+1)**2
    segundo2 = (enemenoska+1)*alfa*beta
    segundo = segundo1 - segundo2

    if primero == countb and segundo == (counta + countb):
        Good=Good+1
        print("Wii","N°",Good,"--",a,b,n,)
    else:
        Bad=Bad+1
        print("Ño","N°",Bad,"--",a,b,n,)


print("Good",Good)
print("Bad", Bad)
