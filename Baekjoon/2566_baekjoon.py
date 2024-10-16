import sys
input = sys.stdin.readline

a = []
maxN = 0
indexR = 0
indexC = 0
for _ in range(9):
  a.append(list(map(int,input().split())))

for i in a:
  for j in i:
    if j >= maxN :
      maxN = j
      indexR = a.index(i)+1
      indexC = i.index(j)+1

print(maxN)
print(indexR, indexC)

