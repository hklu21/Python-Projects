N = 1024 - int(input())

dp = [0] * (N + 1)
for i in range(1, min(4, N)):
    dp[i] = i
if N >= 4:
    for i in range(4, min(N, 16)):
        dp[i] = min(dp[i - 4], dp[i - 1]) + 1
if N >= 16:
    for i in range(16, min(N, 64)):
        dp[i] = min(dp[i - 16], min(dp[i - 4], dp[i - 1])) + 1
if N >= 64:
    for i in range(64, N + 1):
        dp[i] = min(dp[i - 64], min(dp[i - 16], min(dp[i - 4], dp[i - 1]))) + 1
if N > 0:
    print(dp[-1])
else:
    print(0)