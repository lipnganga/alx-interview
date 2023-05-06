import math

def minOperations(n):
    if n == 1:
        return 0

    # Initialize the array to store minimum number of operations
    dp = [float('inf')] * (n+1)
    dp[1] = 0

    # Fill up the array iteratively
    for i in range(2, n+1):
        for j in range(1, int(math.sqrt(i))+1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i//j))

    # Return the minimum number of operations required to obtain n H characters
    return dp[n] if dp[n] != float('inf') else 0
