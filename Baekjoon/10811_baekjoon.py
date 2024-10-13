import sys
input = sys.stdin.readline

n,m = map(int, input().split())
result = [*range(n+1)[1:]]

for _ in range(m):
  i,j = map(int, input().split())
  if i == 1:
    result[i-1:j] = result[j-1::-1]
  else:
    result[i-1:j] = result[j-1:i-2:-1]

print(' '.join(map(str,result)))