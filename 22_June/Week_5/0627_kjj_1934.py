
n = int(input())

def gcd(a,b):
    if b == 0:
        return a
    else: # else 지워도 동작 똑같아용
        return gcd(b, a % b)

for i in range(n):
    a , b = map(int, input().split())
    g = gcd(a,b)
    print(int(g*(a/g)*(b/g)))

## 깔꼼하네여!!!
## 👍