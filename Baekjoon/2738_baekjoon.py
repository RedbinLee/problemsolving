import sys
input = sys.stdin.readline

n,m = map(int, input().split())

a = []
b = []

for _ in range(n):
  a.append(list(map(int, input().split())))

for _ in range(n):
  b.append(list(map(int, input().split())))

result = []
for i in range(n):
  result.append(list(x+y for x,y in zip(a[i],b[i])))

for i in range (n):
  c_list = list(map(str, result[i]))
  print(' '.join(c_list))
