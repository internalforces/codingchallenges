def solution(board, h, w):
    answer = 0
    if h-1 != -1 and board[h][w] == board[h-1][w]:
        answer+=1
    if h+1 != len(board) and board[h][w] == board[h+1][w]:
        answer+=1
    if w-1 != -1 and board[h][w] == board[h][w-1]:
        answer+=1
    if w+1 != len(board) and board[h][w] == board[h][w+1]:
        answer+=1
    return answer