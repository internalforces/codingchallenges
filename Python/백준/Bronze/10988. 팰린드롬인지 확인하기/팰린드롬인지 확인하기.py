import sys

input = sys.stdin.readline

word = input().strip()

word_reverse = word[::-1]

if word == word_reverse:
    print(1)
else:
    print(0)
