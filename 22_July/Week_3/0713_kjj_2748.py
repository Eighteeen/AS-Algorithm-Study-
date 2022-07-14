n = int(input())

fn = [0 for i in range(n+2)]

fn[1] = 1

for i in range(2, n+2):
    fn[i] = fn[i-1] + fn[i-2]

print(fn[i-1])