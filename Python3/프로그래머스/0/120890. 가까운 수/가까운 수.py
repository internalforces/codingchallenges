def solution(array, n):
    temp = []
    for idx, num in enumerate(array):
        temp.append([abs(n - num),idx,n-num])
    temp.sort(key=lambda x:(x[0],-x[2]))
    return array[temp[0][1]]