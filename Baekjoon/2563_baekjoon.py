import sys
input = sys.stdin.readline

n = int(input())

total = n * 100

l = []

for _ in range(n):
  l.append(list(map(int, input().split())))

for i in range(n-1):
  for j in range(i+1,n):
    # print("i,j",i,j)
    xdiff = abs(l[i][0] - l[j][0])
    ydiff = abs(l[i][1] - l[j][1])
    # print(xdiff, ydiff)
    if xdiff < 10 and ydiff < 10:
      diff = (10-xdiff) * (10-ydiff)
      # print("diff",diff)
      total -= diff

print(total)