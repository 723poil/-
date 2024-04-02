def solution():
    if dp == 1:
        return 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return(dp[n])

n = int(input())
dp = [0] * (n+1)

print(solution())
