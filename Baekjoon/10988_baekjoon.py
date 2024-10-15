import sys
input = sys.stdin.readline

p = input().rstrip()

if p == p[-1::-1]:
  print(1)
else:
  print(0)