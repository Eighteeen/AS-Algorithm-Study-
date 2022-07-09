# *2

find_str = input()
cnt_ring = int(input())
find_ring = 0

for _ in range(cnt_ring):
    s1 = input()
    s = s1 * 2
    
    for i in range(len(s)):
        if find_str == s [i:i+len(find_str)]:
            find_ring +=1
            break

print(find_ring)

## 부분문자열 in 문자열로 할 수 있슴다