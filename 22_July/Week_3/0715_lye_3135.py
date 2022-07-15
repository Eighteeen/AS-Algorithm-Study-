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

## kjh 코드처럼 아예 (gap+1) 값을 기준으로 최소값을 구했다면 if문을 덜 써도 됐었을 것 같습니다
## 만약 불가피하게 이런 if문을 써야만한다면, +1 할지 말지 여부를 결정하는 Bool 변수를 추가로 사용하는게 직관적이라고 생각합니다. 변수 하나 더 만들어봤자 몇십억 바이트 중 4바이트 더 쓰는거기도하고요
if targetBtn != 1001:
	print(gap + 1)
else:
	print(gap)
	
## 👍
