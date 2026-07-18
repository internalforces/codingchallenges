def solution(my_string, letter):
    for i in letter:
        my_string = my_string.replace(i,"")
    return my_string