def solution(quiz):
    answer = []
    
    for i in quiz:
        left, right = i.split("=")
        a, op, b = left.split()
        
        if op == "+":
            if int(a) + int(b) == int(right):
                answer.append("O")
            else:
                answer.append("X")
        elif op == "-":
            if int(a) - int(b) == int(right):
                answer.append("O")
            else:
                answer.append("X")
    return answer