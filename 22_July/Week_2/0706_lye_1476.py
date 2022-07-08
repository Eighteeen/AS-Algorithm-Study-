E, S, M = map(int, input().split(' '))
if E==15: E=0
if S==28: S=0
if M==19: M=0
i = 0

while True:
	if E+S+M == 0: 
		print("7980") 
		break
	nowNum = 28 * i + S
	if (nowNum % 15 == E) and (nowNum % 19 == M):
		print(nowNum)
		break
	i += 1

## 효율적으로 풀려하신 노력이 보이는군요
