# [백준] 2864번 - 5와 6의 차이
# 블로그 주소 : https://tteum.tistory.com/278


import sys

a, b = map(str, sys.stdin.readline().split())

a = a.replace('6','5')
b = b.replace('6','5')
min = int(a) + int(b)

a = a.replace('5','6')
b = b.replace('5','6')
max = int(a) + int(b)

print(min,max)