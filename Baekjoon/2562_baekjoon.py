import sys
input = sys.stdin.readline

l = []

for _ in range(9):
  l.append(int(input()))

m = sorted(l)[-1]
print(m)
print(l.index(m)+1)
