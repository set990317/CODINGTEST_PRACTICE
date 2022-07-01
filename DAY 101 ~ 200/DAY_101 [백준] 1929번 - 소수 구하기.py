def sosu (num):
    cnt = 0
    for i in range(num+1,(num*2)+1):
        check = 0
        if i == 1 :
            continue
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                check = 1
                break
        if check == 0 :
            cnt += 1
    return cnt
n = int(input())
while(n != 0):

    count = sosu(n)
    print(count)
    n = int(input())