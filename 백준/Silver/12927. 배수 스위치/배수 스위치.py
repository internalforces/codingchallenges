swith_yn = list((input()))

swith_yn.insert(0, 'N')

answer = 0
for i in range(len(swith_yn)):
    if swith_yn[i] == 'Y':
        for j in range(i, len(swith_yn), i):
            if swith_yn[j] == 'Y':
                swith_yn[j] = 'N'
            else:
                swith_yn[j] = 'Y'

        answer += 1

print(answer)