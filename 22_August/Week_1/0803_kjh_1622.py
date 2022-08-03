while True:
  try:
    a, b = input(), input()
  except EOFError:
    break

  a_alphabet_used_count, b_alphabet_used_count = [0] * 26, [0] * 26
  for alphabet in a:
    a_alphabet_used_count[ord(alphabet) - ord('a')] += 1
  for alphabet in b:
    b_alphabet_used_count[ord(alphabet) - ord('a')] += 1
  
  for i in range(26):
    min_used_count =  min(a_alphabet_used_count[i], b_alphabet_used_count[i])
    alphabet = chr(ord('a') + i)
    print(alphabet * min_used_count, end='')
  print()