memoization = [[0 for j in range(15)] for i in range(15)]
## 이걸 재귀로 푸시다니,,,!
## 굳굳~
def count_residents(floor, unit):
    if memoization[floor][unit] != 0: return memoization[floor][unit]
    if floor == 0: return unit
    
    count = 0;
    for i in range(1, unit + 1):
        count += count_residents(floor - 1, i)
    
    memoization[floor][unit] = count
    return count


T = int(input())

for i in range(T):
    floor = int(input())
    unit = int(input())

    print(count_residents(floor, unit))
