playername = input('Enter a player name: ')
oc = input('Enter an offensive category: ')
fhandle = open('fangraphs_leaderboard.csv', 'r', encoding = 'utf-8-sig')
content = [item.replace('"','').replace('\n','').split(',') for item in fhandle.readlines()]
if oc in content[0]:
	ocindex = content[0].index(oc)
else:
	exit('Category not available')
counter = len(content)
for line in content:
	if playername in line:
		print(playername, line[1], line[ocindex],sep = ', ')
		break
	else:
		counter -= 1
if counter == 0: print('Player not found') #Is there a more efficient way to do this?
fhandle.close()
