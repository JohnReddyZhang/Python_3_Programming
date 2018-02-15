import math
# import sys
pointlst = []
while True:
	point = input('Enter a point: ')
	if point =='':
		break
	else:
		pointlst.append(tuple(int(num) for num in point.split(',')))
		#method inspired by https://stackoverflow.com/questions/3371269/call-int-function-on-every-list-element
# print(pointlst, file=sys.stderr)
destlst =[]
for item in pointlst:
	destlst.append(math.sqrt((item[0]-0)**2+(item[1]-0)**2))
fhandle = open(input('Enter a dest file path: '),'w')
fhandle.truncate()
for i in range(len(pointlst)):
	fhandle.write(str(pointlst[i]) + ': ' + str(destlst[i])+'\n')
fhandle.close()

