lst = []
while True:
	item = input('Please enter a string:')
	if item =='':
		break
	else:
		lst.append(item)
print(sorted(lst))