def calc_combinations_to_choose_m_from_n(m, n):
    return factorial(n) // (factorial(m) * factorial(n - m))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

T = int(input())

for _ in range(T):
    m, n = map(int, input().split())
    print(calc_combinations_to_choose_m_from_n(m, n))