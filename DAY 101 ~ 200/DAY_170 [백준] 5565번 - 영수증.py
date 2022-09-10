# [백준] 5565번 - 영수증
# 블로그 주소 : https://tteum.tistory.com/327

import sys

receipt = []

for _ in range(10):
    receipt.append(int(sys.stdin.readline()))

book = sum(receipt) - receipt[0]

print(receipt[0] - book)