import re
usrinput = input('Enter a sentence: ')
lst = re.split('\s|,\s',usrinput) 
print(lst)
dic = dict()
for item in lst:
	if item in dic:
		dic[item] = dic[item] + 1
	else:
		dic[item] = 1
maxcount = max(dic.values())
#print(maxcount)
#print(dic)
for key,value in dic.items():
	if value == maxcount:
		print(key)
		print(value)
