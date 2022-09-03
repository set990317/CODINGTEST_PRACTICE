# [백준] 2490번 - 윷놀이
# 블로그 주소 : https://tteum.tistory.com/316

import sys

dic = {1:'A',2:'B',3:'C',4:'D',0:'E'}

for _ in range(3):
    yut = list(map(int,sys.stdin.readline().split()))
    num = yut.count(0)
    print(dic[num])