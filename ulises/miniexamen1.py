#Mini examen 1
#Ulises Bruno Lozano
#13/12/16
a=input("Ingresa cualquier cantidad de numeros enteros: ")
def miniexamen(x):
    x=a
    lista=[]
    impares=[]
    for e in x:
        lista.append(e)
    for i in lista:
        if i%2==1:
            impares.append(i)
            impares.sort()
    print impares[-1]
output=miniexamen(a)
