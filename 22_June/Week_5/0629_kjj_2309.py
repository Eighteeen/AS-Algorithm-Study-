# 전체에서 두명뺀 조합 = 100
# 하나의 리스트에서 여러조합을 구할때: itertools 사용!

import itertools

dwarf = [int(input()) for _ in range(9)]

for i in itertools.combinations(dwarf, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break
## 오와 이런기능이 있었어?
