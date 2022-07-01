fruitCnt,snakeLen = map(int, input().split(' '))
fruitList = list(map(int, input().split(' ')))
fruitList.sort()
for fruit in fruitList:
 if(fruit <= snakeLen):
  snakeLen += 1
print(snakeLen)
