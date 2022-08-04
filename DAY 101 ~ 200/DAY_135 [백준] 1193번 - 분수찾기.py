# [코드업] 1193번 - 분수찾기
# 블로그 주소 : https://tteum.tistory.com/284

X = int(input())
count = 1
total = 2
odd_or_even = False # 1로 시작하는게 True, 아닌게 False 혼자 정한거.

while(True):
    if X-count <= 0:
        break
    else :
        X -= count
        total += 1
        count += 1
        odd_or_even = not odd_or_even

if odd_or_even == True :
    print(str(X)+"/"+str(total-X))
else :
    print(str(total-X)+"/"+str(X))