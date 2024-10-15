import sys
input = sys.stdin.readline

n = int(input())
result = n

for _ in range(n) :
  a = input().rstrip()
  for i in range(len(a)-1):
    if a[i] == a[i+1] :
      pass
    elif a[i] in a[i+1:]:
      result -= 1
      break

print(result)

#출처 tomato9755 baekjoon