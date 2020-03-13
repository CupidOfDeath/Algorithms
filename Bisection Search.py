#Finding the square root of a number using bisection search

x = int(input('Enter the number which you want to find the square root of: '))
epsilon = 0.01
n = 0
low = 1
high = x
g = (low+high) / 2

while abs(g*g-x) >= epsilon:
	if (g*g) > x:
		high = g
	elif (g*g) < x:
		low = g
	g = (low+high) / 2
	n += 1

print('The square root of', x, 'is', g)
print('The number of computations it took is', n)
	

