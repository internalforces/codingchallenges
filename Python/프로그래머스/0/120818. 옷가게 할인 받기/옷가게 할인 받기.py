def solution(price):
    if price >= 100_000 and price < 300_000:
        return (price * 0.95)//1
    elif price >= 300_000 and price  < 500_000:
        return (price * 0.9)//1
    elif price >= 500000:
        return (price * 0.8)//1
    else:
        return price