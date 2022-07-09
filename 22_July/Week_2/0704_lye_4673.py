def getDigitSum(num):
	strNum = str(num)
	sum = num
	for i in strNum:
		sum += int(i)
	return sum
	
isSelfNum = []

for i in range(0, 10000):
	isSelfNum.append(False);

for i in range(1, 10001):
	digitSum = getDigitSum(i)
	if digitSum < 10001:
		isSelfNum[digitSum-1] = True;
	
for i in range(0, 10000):
	if isSelfNum[i] == False:
		print(i+1)

## 로나코로 힘들텐데 굳이네여~~