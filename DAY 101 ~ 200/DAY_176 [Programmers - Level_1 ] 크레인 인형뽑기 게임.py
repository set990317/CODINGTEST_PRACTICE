# [프로그래머스 Level 1] - 크레인 인형뽑기 게임
# 블로그 주소 : https://tteum.tistory.com/352

def solution(board, moves):
    answer = 0
    stack = []
    
    for i in range(len(moves)):
        tmp = moves[i]-1
        for j in range(len(board)):
   
            if board[j][tmp] != 0:
                if len(stack) != 0 :
                    if stack[-1] == board[j][tmp] :
                        stack.pop()
                        answer += 2 
                    else :
                        stack.append(board[j][tmp])  
                else :
                    stack.append(board[j][tmp])                   

                board[j][tmp] = 0    
                break
    
    return answer