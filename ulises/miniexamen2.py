#Miniexamen 2
#Ulises Bruno Lozano
#13/12/16
a=raw_input("Ingresa una palabra: ")
def miniexamen2(x):
    x=a
    lista=[]
    for e in x:
        lista.append(e)
    lista.reverse()
    print lista
output=miniexamen2(a)
