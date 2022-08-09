voca = input()
result = []

for i in range(1,len(voca)-1 ):
    for j in range( i+1, len(voca)):
        result.append(voca[:i][::-1] + voca[i:j][::-1] + voca[j:][::-1])

print(sorted(result)[0])