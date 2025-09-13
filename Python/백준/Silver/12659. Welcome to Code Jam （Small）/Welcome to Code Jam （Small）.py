import sys

def main():
    input = sys.stdin.readline
    n = int(input().strip())

    for case_idx in range(1, n + 1):
        s = input().rstrip("\n")  # 공백(스페이스)은 살리고 개행만 제거

        # "welcome to code jam"의 위치에 맞춘 DP (0~18)
        dp = [0] * 19
        MOD = 10000

        for ch in s:
            if ch == 'w':
                dp[0] = (dp[0] + 1) % MOD
            elif ch == 'e':
                dp[1]  = (dp[1]  + dp[0])  % MOD
                dp[6]  = (dp[6]  + dp[5])  % MOD
                dp[14] = (dp[14] + dp[13]) % MOD
            elif ch == 'l':
                dp[2]  = (dp[2]  + dp[1])  % MOD
            elif ch == 'c':
                dp[3]  = (dp[3]  + dp[2])  % MOD
                dp[11] = (dp[11] + dp[10]) % MOD
            elif ch == 'o':
                dp[4]  = (dp[4]  + dp[3])  % MOD
                dp[9]  = (dp[9]  + dp[8])  % MOD
                dp[12] = (dp[12] + dp[11]) % MOD
            elif ch == 'm':
                dp[5]  = (dp[5]  + dp[4])  % MOD
                dp[18] = (dp[18] + dp[17]) % MOD
            elif ch == 't':
                dp[8]  = (dp[8]  + dp[7])  % MOD
            elif ch == 'd':
                dp[13] = (dp[13] + dp[12]) % MOD
            elif ch == 'j':
                dp[16] = (dp[16] + dp[15]) % MOD
            elif ch == 'a':
                dp[17] = (dp[17] + dp[16]) % MOD
            elif ch == ' ':
                dp[7]  = (dp[7]  + dp[6])  % MOD
                dp[10] = (dp[10] + dp[9])  % MOD
                dp[15] = (dp[15] + dp[14]) % MOD
            else:
                continue

        print(f"Case #{case_idx}: {dp[18]:04d}")

if __name__ == "__main__":
    main()