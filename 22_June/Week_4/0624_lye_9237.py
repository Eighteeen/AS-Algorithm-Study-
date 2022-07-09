treeCnt = int(input())
treeArr = list(map(int, input().split(' ')))
treeArr.sort(reverse=True)
for i in range(0, treeCnt):
	treeArr[i] += i + 2
print(max(treeArr))
## 👍
