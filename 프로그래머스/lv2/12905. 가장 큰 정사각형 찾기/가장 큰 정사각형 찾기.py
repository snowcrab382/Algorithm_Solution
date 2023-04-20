def solution(board):
    if 1 in board[0] or 1 in board[-1]:
        answer = 1
    else:
        answer = 0
        
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j],board[i][j-1],board[i-1][j-1]) + 1
                answer = max(answer, board[i][j])
    return answer ** 2