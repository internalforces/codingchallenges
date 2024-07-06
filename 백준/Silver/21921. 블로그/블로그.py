def max_visitors(N, X, visitors):
    current_sum = sum(visitors[:X])
    max_sum = current_sum
    max_count = 1

    for i in range(X, N):
        current_sum += visitors[i] - visitors[i - X]
        if current_sum > max_sum:
            max_sum = current_sum
            max_count = 1
        elif current_sum == max_sum:
            max_count += 1

    if max_sum == 0:
        return "SAD"
    else:
        return f"{max_sum}\n{max_count}"

N, X = map(int, input().split())
visitors = list(map(int, input().split()))

print(max_visitors(N, X, visitors))
