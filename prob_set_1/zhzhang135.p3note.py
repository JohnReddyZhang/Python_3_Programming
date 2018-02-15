#This is a solution inspired by http://introcs.cs.princeton.edu/java/13flow/Fibonacci.java.html
n = int(input('Please enter a number:'))
f = 0
g = 1
for i in range(n):
	f = f + g
	g = f - g
	print(f)