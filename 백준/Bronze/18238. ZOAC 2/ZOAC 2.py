data = list(input())

start = 'A'
result = 0

for i in data :
  left_value = ord(start) - ord(i)
  right_value = ord(i) - ord(start)

  if left_value < 0 :
    left_value += 26
  elif right_value < 0 :
    right_value += 26

  result += min(left_value, right_value)
  start = i

print(result)