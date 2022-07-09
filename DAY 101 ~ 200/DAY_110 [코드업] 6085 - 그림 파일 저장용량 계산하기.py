# [코드업] 6085 - 그림 파일 저장용량 계산하기
# 블로그 주소 : https://tteum.tistory.com/250

import sys

w,h,b = map(int,sys.stdin.readline().split())
result = round( w*h*b / 8 / 1024 / 1024, 2)

print('%.2f' % result ,"MB")