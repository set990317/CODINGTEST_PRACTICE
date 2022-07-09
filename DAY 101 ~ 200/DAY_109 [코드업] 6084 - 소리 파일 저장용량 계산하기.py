# [코드업] 6084 - 소리 파일 저장용량 계산하기
# 블로그 주소 : https://tteum.tistory.com/249

import sys

h,b,c,s = map(int,sys.stdin.readline().split())
result = round( h*b*c*s / 8 / 1024 / 1024, 1)
print(result, "MB")