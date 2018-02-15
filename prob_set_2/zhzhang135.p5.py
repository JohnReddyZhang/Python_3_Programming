file = open(input('Please enter a file path: '))
wordcount = 0;
linecount = 0;
worddict = {}
for line in file.readlines():
	linecount += 1
	for word in line.strip().split():
		word = word.lower()
		wordcount += 1
		if word in worddict:
			worddict[word] += 1
		else:
			worddict[word] = 1
print('File Stats:\nWord count: '+str(wordcount)+'\nLine count: '+str(linecount)+'\nMost frequent words:')
maxcount = max(worddict.values())
restlist = list(worddict.values())
while maxcount in restlist:
	restlist.remove(maxcount)
maxcount2 = max(restlist)
for key,value in worddict.items():
	if value == maxcount:
		print(str(key)+' ('+str(value)+')')
	if value == maxcount2:
		print(str(key)+' ('+str(value)+')')