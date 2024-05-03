a = int(input())

m = int(input())
array = list(map(int, input().split()))
array.sort()
count = 0

for i in range(len(array)):
    left, right = i + 1, len(array) - 1  
    while left <= right:
        mid = (left + right) // 2
        if array[i] + array[mid] > m:
            right = mid - 1
        elif array[i] + array[mid] < m:
            left = mid + 1
        else:
            count += 1
            break

print(count)
