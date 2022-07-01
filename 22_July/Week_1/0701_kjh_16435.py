fruits, snake_length = map(int, input().split())
fruit_altitudes = list(map(int, input().split()))

fruit_altitudes.sort()

while fruit_altitudes and fruit_altitudes[0] <= snake_length:
    del fruit_altitudes[0]
    snake_length += 1

print(snake_length)