x,y = map(str, input().split())
rev = int(x[::-1]) + int(y[::-1])
print(int(str(rev)[::-1]))
# 자리수 역순 - 더하기 - 결과값 역순