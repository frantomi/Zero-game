import math
def function(x1):
    while True:
        try:
            value = int(input(x1))
        except :
            print("HUEVON")
            continue
        else:
            break
    return float(value)

while True:

    n2=function("Ceros: ")
    a2=function("Primer valor A: ")
    b2=function("Segundo valor B: ")

    if a2<=b2 :
        print("A no puede ser menor que B ")
        continue

    if a2<=0 or b2<=0 or n2<1:
        print("Valores negativos no aceptados")
        continue

    else:
        break

def trial(a,b,n):
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


    print("-----------------------")
    print("j ->", jota)
    print("k ->", ka)
    print("n-k ->", enemenoska)
    print("alfa ->", alfa)
    print("---------------------")
    print("countb", countb)
    print("counta+b",counta+countb)
    print("-------------")
    print("primero",primero)
    print("Segundo",segundo)
    print("-------------------")
    print("probability",primero,"/",segundo)

    if primero == countb and segundo == (counta + countb):
        print("WIII")

trial(a2,b2,n2)
