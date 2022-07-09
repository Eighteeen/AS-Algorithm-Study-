E, S, M = map(int, input().split())
e, s, m = 0,0,0

max = 15 * 28 * 19

for i in range(max):
    if e >= 15: e = 0
    if s >= 28: s = 0
    if m >= 19: m = 0

    e += 1
    s += 1
    m += 1

    if e == E and s == S and m == M:
        print(i+1)
        break