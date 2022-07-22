testCnt = int(input())

for i in range(0, testCnt):
	candyCnt, boxCnt = map(int, input().split(' '))
	boxList = []
	
	for j in range(0, boxCnt):
		num1, num2 = map(int, input().split(' '))
		boxList.append(num1*num2)
	
	boxList.sort(reverse=True)
	
	for j in range(0, boxCnt):
		if boxList[j] >= candyCnt:
			print(j+1)
			break
		candyCnt -= boxList[j]
		
