import sys
input = sys.stdin.readline

result = []
s = input().strip()
length = len(s)
i = 0

while i < length:
    if s[i] == '<':
        while i < length and s[i] != '>':
            result.append(s[i])
            i += 1
        result.append(s[i])
        i += 1
    elif s[i].isalnum():
        start = i
        while i < length and s[i].isalnum():
            i += 1
        result.append(s[start:i][::-1])
    else:
        result.append(s[i])
        i += 1
result_str = "".join(result)
print(result_str)