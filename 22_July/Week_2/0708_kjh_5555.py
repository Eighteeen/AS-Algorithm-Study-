target_text = input()
target_count = 0

text_count = int(input())
for i in range(text_count):
    linked_text = input() * 2
    if target_text in linked_text:
        target_count += 1

print(target_count)