findWord = input()
ringCnt = int(input())
findWordCnt = 0

for i in range(0, ringCnt):
	nowLine = input()
	startIdx = -1
	for j in range(0, len(nowLine)):
		sameCnt = 0
		for k in range(0, len(findWord)):
			nowIdx = (j + k) % 10
			if nowLine[nowIdx] == findWord[k]:
					sameCnt += 1
		if sameCnt == len(findWord):
			findWordCnt += 1
			break