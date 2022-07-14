# 현재주파수: a, 목표주파수: b
a, b = map(int, input().split())
n = int(input())

mhz = []

for i in range(n):
    mhz.append(abs(int(input()) - b))

print(min(abs(b - a),min(mhz) + 1))