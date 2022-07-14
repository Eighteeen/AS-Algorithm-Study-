target = int(input())
num1 = 0
num2 = 1

for i in range(1, target):
	nextNum = num1 + num2
	num1 = num2
	num2 = nextNum

print(num2)

## 크 깔끔
