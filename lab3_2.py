import math

x = float(input("Введите значение x: "))
z = float(input("Введите значение z: "))

def computeG(x, z):
	g = math.sqrt(12*x**4 - 3*x**3 + x**2 - 5*x + 6) - math.log10(z)**2
	print(g)
	return g

computeG(x, z)