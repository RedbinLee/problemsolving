import sys
input = sys.stdin.readline

l = []
max = 0
result = ""

for _ in range(5):
  a = input().rstrip()
  if max <= len(a):
    max = len(a)
  l.append(a)
  
for i in range(max):
  for j in l:
    if len(j) >= i+1:
      result += j[i]

print(result)