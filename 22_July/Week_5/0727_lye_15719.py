import sys
numCnt = int(input())
numStr = sys.stdin.read()
total = 0

nowTxt = ""

for num in numStr:
	if num != ' ':
		nowTxt += num
		continue
	total += int(nowTxt)
	nowTxt = ""
	
total += int(nowTxt)	
originTotal = int(numCnt * (numCnt - 1) / 2)

print(total - originTotal)
