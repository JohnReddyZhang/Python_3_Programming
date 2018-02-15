string = input("Please enter a string: ")
pureletter = []
for item in string:
	if item.isalpha():
		pureletter.append(item.lower())
true = True
for i in range(0,int(len(pureletter)/2)):
	if pureletter[i] != pureletter[len(pureletter)-1-i]:
		true = False
		break
print(true)
