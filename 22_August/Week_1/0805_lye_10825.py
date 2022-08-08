N = int(input())
scoreList = []

for i in range(N):
	name, kor, eng, mat = input().split(' ')
	scoreList.append({'name': name, 'kor': int(kor), 'eng': int(eng), 'mat': int(mat)})

res = sorted(scoreList, key=lambda x: (-x['kor'], x['eng'], -x['mat'], x['name']))

for i in range(N):
	print(res[i]['name'])
