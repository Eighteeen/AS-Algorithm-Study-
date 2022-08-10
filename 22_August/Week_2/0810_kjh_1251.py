word = input()

best_combined = "z" * 5
for i in range(1, len(word) - 1):
  for j in range(i + 1, len(word)):
    piece1 = word[:i][::-1]
    piece2 = word[i:j][::-1]
    piece3 = word[j:][::-1]
    combined = piece1 + piece2 + piece3

    if (combined < best_combined):
      best_combined = combined

print(best_combined)
