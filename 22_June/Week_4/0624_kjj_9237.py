n = int(input())
ti = sorted(list(map(int, input().split())),reverse = True)
gi = 1

result = 0

for i in range(n):
    if ti[i] + gi > result:
        result = ti[i] + gi
    gi += 1

print(result+1)