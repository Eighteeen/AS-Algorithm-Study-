fruitCnt,snakeLen = map(int, input().split(' '))
fruitList = list(map(int, input().split(' ')))
fruitList.sort()
for fruit in fruitList:
 if(fruit <= snakeLen):
  snakeLen += 1
print(snakeLen)

## 제 kjh 코드보다 이게 더 효율적인 것 같네요 👍👍
## 느낀점: 담부터 변수명을 직관적으로 잘 짜야겠다!!
