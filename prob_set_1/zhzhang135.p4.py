import math
str1 = input('Please enter point 1: ') 
str2 = input('please enter point 2: ')
lst = str1.split(',') + str2.split(',')
intlst = []
for item in lst:
	intlst.append(int(item))
print(str(math.sqrt((intlst[2]-intlst[0])*(intlst[2]-intlst[0])+(intlst[3]-intlst[1])*(intlst[3]-intlst[1]))))
