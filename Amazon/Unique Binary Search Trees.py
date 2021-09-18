
def numTrees(n):
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]
            print(f"dp {dp} dp[i] {dp[i]} dp[j] {dp[j]}")
    return dp[n]
    # Catalan Number  (2n)!/((n+1)!*n!)
    # return math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1))


print(numTrees(3))
