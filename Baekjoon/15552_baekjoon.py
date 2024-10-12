import sys
l = int(sys.stdin.readline().rstrip())
for _ in range(l):
  a,b = map(int, sys.stdin.readline().rstrip().split())
  print(a+b)