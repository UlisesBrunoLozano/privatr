import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(3,-3,100) #100 numeros entre el -3 y el 3
y=x**2
z=x
w=x**3
plt.plot(x,y,linewidth=3,color='r',label='parabola')
plt.plot(z,w,linewidth=3,color='g',label='cubica')
plt.legend()
plt.title('Muchas gracias')
plt.xlabel('Algo')
plt.ylabel('Una funcion de algo')
plt.grid(True)
plt.show()
plt.savefig('grafica.png')


#linewidth = Ancho de linea
#linespace = Lista de numeros entre un rango
#Colores = primera letra en ingles (o=orange...)
#Label = etiqueta dentro de la grafica
#Title = Titulo grafica
#x label = Etiquetas en eje x
#y label = Etiquetas en eje y
#grid = Cuadriculado
#legend = Etiqueta de la grafica
#plt.subplot(2,4,6)
#plt.plot([1,2,3,4],[2,7,4,2])
#linewidth=4,color='b'
#plt.subplot(2,4,3)
#plt.plot(5,6'*r',markersize=16)
#plt.show()
#plt.cla() Limpia

x ^ n del 1 al 15 (150 valores de -1 a 1)
