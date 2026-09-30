def solution(m, musicinfos):
    answer = ''
    
    def replace_melody(melody):
        melody = melody.replace("C#", "c")
        melody = melody.replace("D#", "d")
        melody = melody.replace("F#", "f")
        melody = melody.replace("G#", "g")
        melody = melody.replace("A#", "a")
        
        return melody
    
    def cal_play_time(start, end):
        sh, sm = map(int, start.split(":"))
        eh, em = map(int, end.split(":"))

        return (eh * 60 + em) - (sh * 60 + sm)
    
    m = replace_melody(m)
    answer = "(None)"
    
    max_time = -1
    
    for i in musicinfos:
        start, end, title, melody = i.split(",")
        play_time = cal_play_time(start, end)
        melody = replace_melody(melody)
        
        play = ""
        
        for j in range(play_time):
            play += melody[j % len(melody)]
            
        if m in play:
            if play_time > max_time:
                max_time = play_time
                answer = title
    return answer