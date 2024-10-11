h,m =map(int, input().split())

m -= 45
result_m = (m+60)%60
if m<0 :
  h -= 1

if h<0 :
  h = 23

print(h,result_m)
