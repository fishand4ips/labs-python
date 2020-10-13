import math


fin = open('C:/Users/aleko/Desktop/lab3_3_in.txt', 'r') 
full = fin.readline().split()
x, y, z = int(full[0]), int(full[1]), int(full[2])
fin.close()

def computeFi(x, y, z):
	fi = (((math.cos(x) - math.sin(y))**3) / (math.sqrt(math.tan(z)))) + (math.log(x * y * z))**2
	return fi

fout = open('C:/Users/aleko/Desktop/lab3_3_out.txt', 'w')
fout.write(str(computeFi(x,y,z)))
print("Резульат смотрите в файле lab3_3_out.txt")
fout.close()
