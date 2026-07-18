def solution(number, k):
    answer = str(number)
    i=0
    while i<len(answer)-1 and k>0 :
        if answer[i]< answer[i+1]:
            answer=answer[:i]+answer[i+1:]
            
            
            k=k-1
            if i>0:
                i=i-2
            else:
                i=i-1    
        i=i+1
        
    if k>0 :
        answer=answer[:len(answer)-k]
        
    return answer