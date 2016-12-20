import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-6,2,50)
y=-(x**2)
z=5
w=-4*x
plt.plot(x,y,linewidth=3,color='b',label='Inciso a)')
plt.legend()
plt.title('Inciso a)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
plt.savefig('incisoa.png')
