N = int(input())

grouped_count = 0
for _ in range(N):
    word = input()
    if list(word) == sorted(word, key=word.find):
        grouped_count += 1

print(grouped_count)