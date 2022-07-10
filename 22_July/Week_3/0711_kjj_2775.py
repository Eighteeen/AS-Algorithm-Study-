T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    k_zero = list(range(1,n+1))
    
    for i in range(k):
        for j in range(1,n):
            k_zero[j] += k_zero[j-1]
    print(k_zero[-1])
