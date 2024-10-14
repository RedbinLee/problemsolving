import sys
input = sys.stdin.readline

a,b = map(str, input().split())

for i in range(2,-1,-1):
  if int(a[i])-int(b[i]) > 0:
    print(a[2::-1])
    break
  elif int(a[i])-int(b[i]) < 0 :
    print(b[2::-1])
    break