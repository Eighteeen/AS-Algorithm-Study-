caseCnt = int(input())

for i in range(caseCnt):
 m,n = map(int,input().split(' '))
 m = m if (m < n-m) else n-m
 res = 1
 for j in range(m):
  res *= n
  n -= 1
 for j in range(1, m+1):
  res = int(res / j)
 print(res)

## 뭔가 독자적인 방법으로 푼 것 같네
## 굳굳~
