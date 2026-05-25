def parse_expression(expr):

    left, right = expr.split("=")
    left = left.strip()
    right = right.strip()

    if "+" in left:
        a, b = left.split("+")
        op = "+"
    else:
        a, b = left.split("-")
        op = "-"

    return left, a.strip(), op, b.strip(), right

def to_base(num, base):

    if num == 0:
        return "0"

    result = ""

    while num > 0:
        result = str(num % base) + result
        num //= base

    return result


def solution(expressions):
    answer = []
    
    # 진법 후보 구하기
    max_num = -1
    
    for expr in expressions:
        for num in expr:
            if num.isdigit():
                max_num = max(max_num, int(num))
            
    min_base = max_num + 1
    
    true_list = []
    
    for base in range(min_base, 10):
        is_true = True
        
        for expr in expressions:
            lleft, a, op, b, right = parse_expression(expr)

            if right == "X":
                continue

            a_num = int(a, base)
            b_num = int(b, base)
            right_num = int(right, base)

            if op == "+":
                result = a_num + b_num
            else:
                result = a_num - b_num

            if result != right_num:
                is_true = False
                break
                
        if is_true:
            true_list.append(base)
            
    for expr in expressions:
        left, a, op, b, right = parse_expression(expr)

        if right != "X":
            continue

        results = set()
        
        for base in true_list:
            a_num = int(a, base)
            b_num = int(b, base)

            if op == "+":
                result = a_num + b_num
            else:
                result = a_num - b_num

            results.add(to_base(result, base))

        if len(results) == 1:
            x_value = results.pop()
        else:
            x_value = "?"
        
        answer.append(f"{left} = {x_value}")
    
    return answer