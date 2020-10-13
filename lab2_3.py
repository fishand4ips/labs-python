import math

def computeY(t, k, m):
	y = ((1+t)**(2*k) - math.fabs(3*m))**t + ((t + k + 5*m)/(t*k*m + 1))
	print(y)
	return y

computeY(1, 0, 0)