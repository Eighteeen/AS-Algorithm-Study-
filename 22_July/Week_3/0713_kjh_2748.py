fibo = {
    0: 0,
    1: 1
}
## 한 수 배우고싶은 재귀실력입니다ㅎ
def get_nth_fibo(n):
    if n in fibo:
        return fibo[n]
    
    fibo[n] = get_nth_fibo(n-1) + get_nth_fibo(n-2)
    return fibo[n]

n = int(input())
print(get_nth_fibo(n))
