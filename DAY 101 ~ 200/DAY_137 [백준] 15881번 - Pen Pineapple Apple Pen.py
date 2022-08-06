# [코드업] 15881번 - Pen Pineapple Apple Pen
# 블로그 주소 : https://tteum.tistory.com/286

import sys

N = int(input())

thing = str(sys.stdin.readline())
count = thing.count("pPAp")
print(count)