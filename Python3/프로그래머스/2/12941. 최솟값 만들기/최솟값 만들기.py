def solution(A,B):
    answer = 0
    
    A.sort()
    B.sort()
    B.reverse()
    
    for i in range(len(A)):
        answer = answer + A[i]*B[i]

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    #print('A[min] * B[max] = return(min)')

    return answer