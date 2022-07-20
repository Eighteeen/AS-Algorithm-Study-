listCnt, newScore, rankMaxCnt = map(int, input().split(' '))

if listCnt == 0:
	print(1)
else:
	scoreList = list(map(int, input().split(' ')))
	scoreList.append(newScore)
	scoreList.sort(reverse=True)
	newRank = scoreList.index(newScore) + 1

	if len(scoreList) > rankMaxCnt:
		if scoreList[listCnt] == newScore:
			print(-1)
		else:
			print(newRank)
	else:
		print(newRank)
