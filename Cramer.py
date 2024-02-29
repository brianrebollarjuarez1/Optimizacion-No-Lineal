#Resolver sistemas de ecuaciones nxn por Cramer
#Por Brian R.

#Llenado
def llenadoA(n):
    A = np.identity(n)
    indices = np.arange(n)
    for x in indices:
        for y in indices:
            A[x][y] = float(input("Digite un numero de su matriz: "))
    return A
def llenadob(n):
    b = np.zeros(n)
    indices = np.arange(n)
    for x in indices:
        b[x] = float(input("Digite un numero de su vector de resultados: "))
    return b

#Metodo Cramer
def Cramer(n,A,b):
    x = np.zeros(n)
    detA = np.linalg.det(A)
    indices = np.arange(n)
    for y in indices:
        Ax = np.copy(A)
        Ax[:,y] = b
        detj = np.linalg.det(Ax)
        x[y] = (detj)/detA
    return x
#Programa principal
import numpy as np
n = int(input("Digite la dimension de A: "))
A = llenadoA(n)
b = llenadob(n)
x = Cramer(n,A,b)
print("La solucion de: ",A,"x = ",b.T,"es: ", x.T)

