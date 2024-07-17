x = input()
a = x.count('a')

x += x[0:a-1]

min_value = float("inf")

for i in range(len(x) - (a-1)):
    min_value = min(min_value, x[i:i+a].count('b'))

print(min_value)