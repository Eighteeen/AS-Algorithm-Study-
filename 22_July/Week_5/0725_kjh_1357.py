x, y = input().split()
reversed_x, reversed_y = x[::-1], y[::-1]

added_result = int(reversed_x) + int(reversed_y)
reversed_result = str(added_result)[::-1]
print(int(reversed_result))