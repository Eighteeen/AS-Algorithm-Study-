# 강서 = Nsite/강동 Msite
# 조합
import sys ## import만 하고 안 썼네
import math

T = int(input())
result = 0

for i in range(T):
    Nsite, Msite = map(int, input().split())
    result = math.factorial(Msite) // (math.factorial(Nsite) * math.factorial(Msite - Nsite))
    print(result)

## 👍
