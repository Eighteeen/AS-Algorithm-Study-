
n = int(input())

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

for i in range(n):
    a , b = map(int, input().split())
    g = gcd(a,b)
    print(int(g*(a/g)*(b/g)))
# 함수없이 간단한 방법이 또 있나여,,?