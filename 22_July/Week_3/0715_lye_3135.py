nowNum, targetNum = map(int, input().split())
gap = abs(nowNum - targetNum)
btnCnt = int(input())
targetBtn = 1001

for i in range(0, btnCnt):
	nowBtn = int(input())
	nowGap = abs(nowBtn - targetNum)
	if nowGap < gap:
		gap = nowGap
		targetBtn = nowBtn

if targetBtn != 1001:
	print(gap + 1)
else:
	print(gap)
	
