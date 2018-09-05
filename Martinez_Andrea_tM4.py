import numpy as np
import matplotlib.pylab as plt

# Primero punto
n_puntos=1000
x=np.linspace(-1,1,n_puntos)
h= x[1]-x[0]

def factorial(n):
	if n==0:
		a=1
		return a
	else:
		b= n*factorial(n-1)
		return b
y= factorial(5)
print y

def funcion(x,n):
	fun= (1/((2.**n)*(factorial(n))))*((x**-1)**n)
	return fun
fo=[funcion(x,0)]
f1=[funcion(x,1)]
f2=[funcion(x,2)]

plt.plot(x,f0)
plt.plot(x,f1)
plt.plot(x,f2)
plt.show()

	
#Tercer Punto.
w=funcion(x,0)
plt.plot(x,w)
plt.show()

#Cuarto Punto
def derivada (x):
	deri= (funcion(x+h)-funcion(x-h))/(2.0*h)
	return deri

