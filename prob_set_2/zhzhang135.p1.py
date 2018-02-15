file1 = input('Please enter file path 1: ')
file2 = input('Please enter file path 2: ')
lines1 = open(file1).readlines();
lines2 = open(file2).readlines();
linecount = max(len(lines1),len(lines2))
linecomp = list(zip(lines1, lines2))
for item in linecomp:
	if item[0] != item[1]:
		print(linecomp.index(item), end = ', ')
if len(linecomp) < linecount:
	for i in range(len(linecomp), linecount):
		print(i, end = ', ')

