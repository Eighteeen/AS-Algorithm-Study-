fruits, snake_length = map(int, input().split())
fruit_altitudes = list(map(int, input().split()))

fruit_altitudes.sort()
## 오 생각해보지 못한 방식이에요 신선해!
while fruit_altitudes and fruit_altitudes[0] <= snake_length:
    del fruit_altitudes[0]
    snake_length += 1

print(snake_length)

## Welcome to python world😊
## 홍태식이 돌아왔구나~!!