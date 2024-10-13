import sys
input = sys.stdin.readline

n,m = map(int, input().split())
result = [0 for _ in range(n)]
for _ in range(m):
  i,j,k = map(int, input().split())
  change = [k for _ in range(j-i+1)]
  result[i-1:j] = change

print(' '.join(map(str, result)))