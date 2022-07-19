n = int(input())
new = n
cycle = 0

while 1:
    sum_new = (new // 10) + (new % 10)
    new_num = ((new % 10) * 10) + (sum_new % 10) ## new_num 없이 new 변수만 써도 정답으로 잘 나와요 https://www.acmicpc.net/source/46282831
    cycle += 1

    if(new_num == n):
        break
    new = new_num
    
print(cycle)
##긋긋이에여
