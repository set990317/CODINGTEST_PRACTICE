# [백준] 2839번 - 설탕 배달
# 블로그 주소 : https://tteum.tistory.com/231

sugar = int(input())
count = 0

while True:
    if (sugar % 5) == 0:
        count = count + (sugar//5)
        print(count)
        break
    sugar = sugar - 3
    count += 1

    if sugar < 0:
        print("-1")
        break