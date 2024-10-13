import sys
input = sys.stdin.readline

n,m = map(int, input().split())
result = [*range(n+1)[1:n+1]]

for _ in range(m):
  i,j = map(int, input().split())
  tmp = result[i-1]
  result[i-1] = result[j-1]
  result[j-1] = tmp

print(*result) # '*'는 리스트와 같은 container type을 unpacking 하는 역할을 합니다.