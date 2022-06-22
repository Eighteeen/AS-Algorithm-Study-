numArr = [int(c) for c in input()]

for i in range(0, len(numArr)):
	for j in range(0, len(numArr)-1):
		if(numArr[j] < numArr[j+1]):
			tmp = numArr[j]
			numArr[j] = numArr[j+1]
			numArr[j+1] = tmp
for n in numArr:
	print(n, end='')
