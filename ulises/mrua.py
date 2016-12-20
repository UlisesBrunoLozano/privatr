import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(1,-1,150)
for n in range(1,16):
    y=x**n
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
    nombre="grafica"+str(n)+".png"
    plt.savefig('nombre')
