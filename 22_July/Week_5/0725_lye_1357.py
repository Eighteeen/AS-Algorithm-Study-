def reverseNum(num):
 rev_list = list(num)
 rev_list.reverse()
 res = ''.join(rev_list)
 return int(res)

num1, num2 = input().split(' ')
res = reverseNum(num1) + reverseNum(num2)
print(reverseNum(str(res)))
## 🫡
