diction = {}
count = 0
while True:
	item = input('Please enter an integer:')
	if item =='':
		break
	else:
		diction[item] = count
		count += 1
keylst = sorted(diction.keys())
for item in keylst:
	print(str(item)+'('+str(diction[item])+')')