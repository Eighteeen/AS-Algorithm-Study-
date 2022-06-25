# 모묙의 수 n
# 나무가 자라는 일수 ti
# 오래걸리는 것부터 심기 - 내림차순 정렬
# 자라는 최대일 수: 심는 날 + 성장날 
# 이장님 오시는 날 +1




n = int(input())
ti = sorted(list(map(int, input().split())),reverse = True)
gi = 1

result = 0

for i in range(n):
    if ti[i] + gi > result:
        result = ti[i] + gi
    gi += 1

print(result+1)