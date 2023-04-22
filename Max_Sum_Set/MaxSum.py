def findMaxSum(arr):
  
    N = len(arr)
    # Declare dp array
    dp = [[0 for i in range(2)] for j in range(N)]
      
    if (N == 1): 
        return arr[0]
    
    # Initialize the values in dp array
    dp[0][0] = 0
    dp[0][1] = arr[0]
    
    # Loop to find the maximum possible sum
    for i in range(1,N):
        dp[i][1] = dp[i - 1][0] + arr[i]
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])
    
    # Return the maximum sum
    return max(dp[N - 1][0], dp[N - 1][1])
  

print(findMaxSum([-1, -1, 0]))
print(findMaxSum([-1, -1, -10, -34]))
print(findMaxSum([7,2,5,8,6]))