#등차수열 문제라는 것을 파악하는 것이 중요하다.

import sys
import math

input = sys.stdin.readline
a,b,v = map(int, input().split())

print(math.ceil(((v-a)/(a-b))+1))