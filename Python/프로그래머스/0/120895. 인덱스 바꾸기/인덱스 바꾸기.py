def solution(my_string, num1, num2):
    # 문자열을 리스트로 변환
    arr = list(my_string)

    # 인덱스 num1과 num2에 해당하는 문자 가져오기
    str1 = arr[num1]
    str2 = arr[num2]

    # 두 문자 교환
    arr[num1] = str2
    arr[num2] = str1

    # 리스트를 다시 문자열로 변환하여 반환
    return ''.join(arr)