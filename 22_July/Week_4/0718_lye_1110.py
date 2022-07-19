def SumDigit(num):
	num1 = int(num / 10)
	num2 = num % 10
	return (num2 * 10) + ((num1 + num2) % 10)

originNum = int(input())
nowNum = originNum
cycleCnt = 0

while True:
	nowNum = SumDigit(nowNum)
	cycleCnt += 1
	if nowNum == originNum:
		break
	
print(cycleCnt)
