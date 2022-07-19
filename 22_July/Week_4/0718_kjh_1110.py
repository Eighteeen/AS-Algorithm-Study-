num=int(input())

left, right = num // 10, num % 10
count = 0

while True:
	left, right = right, (left+right)%10
	count = count + 1

	if (left*10 + right) == num:
		break;
 
print(count)

##이렇게 깔끔하게 할수도 있구나,,,,
