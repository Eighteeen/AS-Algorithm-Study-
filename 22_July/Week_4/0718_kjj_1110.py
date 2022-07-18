n = int(input())
new = n
cycle = 0

while 1:
    sum_new = (new // 10) + (new % 10)
    new_num = ((new % 10) * 10) + (sum_new % 10)
    cycle += 1

    if(new_num == n):
        break
    new = new_num
    
print(cycle)