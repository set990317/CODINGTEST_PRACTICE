# [백준] 14681번 - 사분면 고르기
# 블로그 주소 : https://tteum.tistory.com/188

x = int(input())
y = int(input())

if x > 0 and y > 0 :
    print("1")
elif x < 0 and y > 0 :
    print("2")
elif x < 0 and y < 0 :
    print("3")
else : print("4")