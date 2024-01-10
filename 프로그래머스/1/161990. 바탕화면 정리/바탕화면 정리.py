def solution(wallpaper):
    answer = [50, 50, 0, 0]
    
    for y, row in enumerate(wallpaper):
        for x, char in enumerate(row):
            if char == '#':
                answer = [
                            min(answer[0], y), min(answer[1], x),
                            max(answer[2], (y+1)), max(answer[3], (x+1))
                         ]
    return answer

    