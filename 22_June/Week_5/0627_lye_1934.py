# 최소공배수는 A*B/최소공약수 라는 공식을 활용

testCnt = int(input())

def get_GCD(a, b):
	if(a%b==0):
		return b
	return get_GCD(b, a%b)
	
for i in range(0, testCnt):
	a, b = map(int, input().split())
	minNum = (a if a<b else b)
	print(int(a * b / get_GCD(minNum, a+b-minNum)))
	
