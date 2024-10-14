import sys
input = sys.stdin.readline

original = [1, 1, 2, 2, 2, 8]

found = list(map(int, input().split()))

result = []

for i in range(6):
  result.append(original[i]-found[i])

print(*result)