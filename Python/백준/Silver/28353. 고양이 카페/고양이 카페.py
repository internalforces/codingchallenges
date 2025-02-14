import sys

def happyninggen(numbers, k):
    numbers.sort()  
    happy_count = 0
    left = 0
    right = len(numbers) - 1

    while left < right:  
        if numbers[left] + numbers[right] <= k:
            happy_count += 1  
            left += 1
            right -= 1  
        else:
            right -= 1  

    return happy_count  

n, k = map(int, sys.stdin.readline().split())  
numbers = list(map(int, sys.stdin.readline().split()))  


result = happyninggen(numbers, k)
print(result)