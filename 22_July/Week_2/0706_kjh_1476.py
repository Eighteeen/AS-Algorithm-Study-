target_e, target_s, target_m = map(int, input().split())

##앗,,,이런방법이
e, s, m = 1, 1, 1
year = 1

while e != target_e or s != target_s or m != target_m:
    e = e%15 + 1
    s = s%28 + 1
    m = m%19 + 1
    year += 1

print(year)
