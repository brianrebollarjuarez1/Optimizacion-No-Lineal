#Aproximacion de minimos de funciones por acotamiento de intervalos.
#Por Brian R.
#Funcion a minimizar
def funcion(x):
    fx = pow(x,2) + 4
    return fx
#Acotamiento de intervalos
def acotinter(a,b,L):
    pmab = (a + b)/2
    ab1 = a + (L/4)
    ab2 = b - (L/4)
    return pmab,ab1,ab2
#Cambio de intervalos
def cambinter(a,b,ab1,ab2,pmab,fab1,fab2,fpmab):
    if fab1 < fpmab:
        b = pmab
        pmab = ab1
        fpmab = fab1
    else:
        if fab2 < fpmab:
            a = pmab
            pmab = ab2
            fpmab = fab2
        else:
            a = ab1
            b = ab2
    return a,b,ab1,ab2,pmab,fab1,fab2,fpmab
    
a = float(input("Digite el extremo inferior del intervalo: "))
b = float(input("Digite el extremo superior del intervalo: "))
L = b - a
while L > 0.0002:
    pmab,ab1,ab2 = acotinter(a, b, L)
    fab1 = funcion(ab1)
    fab2 = funcion(ab2)
    fpmab = funcion(pmab)
    a,b,ab1,ab2,pmab,fab1,fab2,fpmab = cambinter(a,b,ab1,ab2,pmab,fab1,fab2,fpmab)
    L = b - a
print("El minimo de la funcion es: ", [pmab,fpmab])
    