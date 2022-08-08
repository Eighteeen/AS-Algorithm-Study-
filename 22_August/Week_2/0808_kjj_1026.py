from re import T


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = 0

a.sort(reverse = True)
b_index = sorted(range(n), key = lambda x: b[x])

for i in range(n):
    mul = a[i] * b[b_index[i]]
    s += mul

print(s)