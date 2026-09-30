def solution(p):
    if p == "":
        return p
    
    u, v = True, 0
    for i in range(len(p)):
        if p[i] == "(":
            v += 1
        else:
            v -= 1
        if v < 0:
            u = False
        if v == 0:
            if u:
                return p[:i+1] + solution(p[i+1:])
            else:
                return "(" + solution(p[i+1:]) + ")" + ''.join(list(map(lambda x : '(' if x == ')' else ')', p[1:i])))
            