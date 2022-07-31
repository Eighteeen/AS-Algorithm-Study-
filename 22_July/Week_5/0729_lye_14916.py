num = int(input())
res = int(num / 5)
num = num % 5

while True:
	if num == 0:
		break;
	if num % 2 == 0:
		res += int(num / 2)
		num = num % 2
	else:
		num += 5
		res -= 1
	if res < 0:
		res = -1
		break

print(res)
