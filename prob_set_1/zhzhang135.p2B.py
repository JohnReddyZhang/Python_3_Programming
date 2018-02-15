userinput = input("Please enter some words: ")
lst = userinput.split(' ')
for item in lst:
	if item[0] == 's':
		#print(item[0])
		continue
	else:
		print(item)