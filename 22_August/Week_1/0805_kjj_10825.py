n = int(input())

students = []
for _ in range(n):
    students.append(input(). split())

rank = sorted(students, key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in rank:
    print(i[0])

## 올 배열로 하는것도 심플하고 좋네요

#다른 방법을 통한 시간 단축 가능하신분,,?
## -> 랭킹쪽에서 다른 사람들 코드 볼 수 있어
