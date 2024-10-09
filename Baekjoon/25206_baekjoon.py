n = 20
subjectDic = {
  "A+" : 4.5,
  "A0" : 4,
  "B+" : 3.5,
  "B0" : 3,
  "C+" : 2.5,
  "C0" : 2,
  "D+" : 1.5,
  "D0" : 1,
  "F" : 0,
}

"(학점 × 과목평점)의 합을 학점의 총합으로 나눈 값"
sum1 = 0
sum2 = 0
for i in range(20):
  s = input().split()
  if s[-1] == "P" :
    n -= 1
  else:
    sum1 += float(s[1]) * subjectDic[s[-1]]
    sum2 += float(s[1])

print(sum1/sum2)