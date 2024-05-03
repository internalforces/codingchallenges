n = int(input())
arr = list(map(int, input().split()))

arr.sort()
min_sum = float('inf')
result = None

left = 0
right = n - 1

while left < right:
    current_sum = arr[left] + arr[right]
    if abs(current_sum) < min_sum:
        min_sum = abs(current_sum)
        result = arr[left] + arr[right]
    if current_sum < 0:
        left += 1
    elif current_sum > 0:
        right -= 1
    else:
        break

print(result)