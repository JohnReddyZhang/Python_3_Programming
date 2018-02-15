n = int(input('Please enter a number:'))
if n == 1: print(1)
else:
	m = 1
	g = 1
	print(m)
	print(g)
	for i in range(2,n):
		out = m + g
		m = g
		g = out
		print(out)
		