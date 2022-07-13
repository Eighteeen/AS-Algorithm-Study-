testCnt = int(input())

for i in range(0, testCnt):
	k = int(input())
	n = int(input())
	numArr = list(range(1, n+1))
	for j in range(0, k):
		for k in range(0, n-1):
			numArr[k+1] = numArr[k]+ numArr[k+1]
	print(numArr[len(numArr)-1])
