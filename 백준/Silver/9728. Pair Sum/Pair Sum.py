a = int(input())
for i in range(a):
    n, m = map(int, input().split())
    array = list(map(int, input().split())) 
    left, right = 0, n - 1  
    count = 0
    
    while left < right:
        if array[left] + array[right] > m:
            right -= 1
        elif array[left] + array[right] < m: 
            left += 1
        else:
            count += 1
            left += 1
            
    print("Case #%d: %d"%(i+1,count))
