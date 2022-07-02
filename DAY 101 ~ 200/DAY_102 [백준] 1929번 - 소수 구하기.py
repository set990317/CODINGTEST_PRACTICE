def sosu(number):
    for j in range(2,int(number**0.5)+1):
        if number % j == 0:
            return 0
    return 1

def jinsu(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력    

def solution(n, k):
    answer = 0
    n = jinsu(n,k)
    n = str(n).split("0")
    
    for i in range(len(n)):
        if n[i] == "1" or n[i] == '':
            continue
        number = int(n[i])
        
        if sosu(number) == 1:
            answer += 1

    return answer