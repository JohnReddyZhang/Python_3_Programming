fhandle = open('fangraphs_leaderboard.csv', 'r', encoding = 'utf-8-sig')
content = [item.replace('"','').replace('\n','').split(',') for item in fhandle.readlines()]
oc = input('Enter an offensive category: ')
if oc in content[0]:
	ocindex = content[0].index(oc)
else:
	fhandle.close()
	exit('Category not available')
scorelst = []
for line in content[1:]:
	if '%' in line[ocindex]:
		scorelst.append((float(line[ocindex].rstrip(' %')),line[0],line[ocindex]))
	else:
		scorelst.append((float(line[ocindex]),line[0],line[ocindex]))
highest5 = sorted(scorelst, reverse = True)[:5]
print('Result:')
for element in highest5:
	print(element[1],element[2], sep = ', ')