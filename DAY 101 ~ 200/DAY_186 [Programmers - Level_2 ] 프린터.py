# [프로그래머스 Level 2] - 프린터
# 블로그 주소 : https://tteum.tistory.com/370

def solution(priorities, location):
    answer = 0
    
    while (len(priorities) != 0):
    	# 가장 앞에 있는 문서가 중요도가 제일 높은 경우
        if priorities[0] == max(priorities):
            del priorities[0]
            answer += 1
            
            # 프린트된게 그 문서라면!
            if location == 0 :
                break
            else :
                location -= 1
                
        # 뒤에 중요도가 높은 문서가 있다면
        else:
            priorities.append(priorities[0])
            priorities = priorities[1:len(priorities)]
            
            # 뒤로 옮겨진 게 그 문서였다면!
            if location == 0:
                location = len(priorities) - 1
            else :
                location -= 1
    
    return answer