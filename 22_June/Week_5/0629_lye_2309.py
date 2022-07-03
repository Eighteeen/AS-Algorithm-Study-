dwarfCnt = 9
dwarfList = [ ]
for i in range(0, dwarfCnt):
 dwarfList.append(int(input()))
leftValue = sum(dwarfList)-100
for i in range(0, dwarfCnt):
  for j in range(i+1, dwarfCnt):
   if dwarfList[i] + dwarfList[j] == leftValue:
    dwarfList.remove(dwarfList[j])
    dwarfList.remove(dwarfList[i])
    break;
  if len(dwarfList)!=dwarfCnt:
    break;
dwarfList.sort()
for n in dwarfList:
 print(n)
