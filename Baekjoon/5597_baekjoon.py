import sys
input = sys.stdin.readline

result = [*range(32)[1:-1]]
for _ in range(28):
  result.remove(int(input().rstrip()))
print(result[0])
print(result[1])