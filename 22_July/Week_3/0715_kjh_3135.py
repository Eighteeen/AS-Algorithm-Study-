from_hz, to_hz = map(int, input().split())

least_diff = abs(from_hz - to_hz)

saved_count = int(input())
for _ in range(saved_count):
    saved_hz = int(input())

    diff = abs(saved_hz - to_hz)
    if diff < least_diff:
        least_diff = diff + 1

print(least_diff)