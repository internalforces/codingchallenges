def GCD(x,y):
    while(y): #y가 참일 동안 = 자연수일 때 =   a%b!=0
        x,y=y,x%y
    return x
def solution(numer1, denom1, numer2, denom2):
    answer = []
    a = numer1*denom2
    b = denom1*denom2
    c = numer2*denom1
    
    d = a+c
    e = GCD(d,b)
    
    
    answer.append(d//e)
    answer.append(b//e)
    return answer