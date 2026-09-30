def solution(cards1, cards2, goal):
    card1 = 0
    card2 = 0
    
    for g in goal:
        if card1 < len(cards1) and cards1[card1] == g:
            card1 += 1
        elif card2 < len(cards2) and cards2[card2] == g:
            card2 += 1
        else:
            return "No"
    return "Yes"
