n = int(input())
pairs = []
for _ in range(n):
    a, b = map(int, input().split())
    pairs.append((a, b))

pairs.sort(key=lambda x: x[0] - x[1], reverse=True)


height = 0
total_sum = 0
mn = float('inf')


for a, b in pairs:
    # 현재 높이를 최소 높이와 비교하여 갱신
    mn = min(mn, height)

    # 높이 증가
    height += a

    # 총합에 현재 높이 추가
    total_sum += height

    # 높이 감소
    height -= b

    # 최소 높이 갱신
    mn = min(mn, height)

result = total_sum - mn * n
print(result)