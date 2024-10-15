import sys
input = sys.stdin.readline

n = int(input())

result = 0

for _ in range(n):
  a = input().rstrip()
  b = [] # this is for figuring out how many different alphabets are in the string.
  c = "" # comparison string

  for i in a:
    if i not in b:
      b.append(i)
    # print(b)

  if len(b) == 1: #ex)aaaaaaaaa
    result += 1

  elif len(a) == len(b): # case 1 all different alphabet  ex)asdfhj
    # print("case1")
    result += 1

  elif len(a) < 3: # case 2 just length 2 ex) ab, fd, ag
    result += 1
    # print("case2")

  else : # case 3
    # create the comparison string c (sorting)
    for i in b:
      for j in a:
        if i == j:
          c += i
    # print("c", c)
    if a == c :
      # print("case ",a,c)
      result += 1

print(result)