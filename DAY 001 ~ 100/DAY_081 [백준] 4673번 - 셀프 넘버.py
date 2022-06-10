# [백준] 4673 - 셀프 넘버 
# 블로그 주소 : https://tteum.tistory.com/216

arr = []

def selfnumber(num):
    n = num
    
    while (n < 10000):
        tmp = sum(list(map(int,str(n))))
        n = n + tmp
        
        if n in arr :
            return 0
        else : arr.append(n)
    return 0

def main():
    for num in range(1,10000):
        if num in arr:
            continue
        selfnumber(num)
        
        if num not in arr :
            print(num)

main()