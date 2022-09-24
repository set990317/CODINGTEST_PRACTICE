# [프로그래머스 Level 2] - 영어 끝말잇기
# 블로그 주소 : https://tteum.tistory.com/367

def solution(n, words):
    answer = []
    tmp = []
    for i in range(len(words)):
        # 1. 단어끼리 제대로 이어지는 지 확인.
        if i != 0 :
            if words[i][0] != words[i - 1][len(words[i - 1]) - 1]:
                if (i + 1) % n == 0:
                    answer = [n, (i + 1) // n]
                else:
                    answer = [(i + 1) % n, ((i + 1) // n) + 1]
                break

        # 2. 같은 단어가 있는 지 확인.
        if words.count(words[i]) > 1:
            if words[i] in tmp:
                if (i + 1) % n == 0:
                    answer = [n, (i + 1) // n]
                else:
                    answer = [(i + 1) % n, ((i + 1) // n) + 1]
                break
            else:
                tmp.append(words[i])

    if answer == []:
        answer = [0, 0]
            
    return answer