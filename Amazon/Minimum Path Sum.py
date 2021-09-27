# grid = [[1,3,1],[1,5,1],[4,2,1]]

# def minPathSum(grid):

#     m, n = len(grid), len(grid[0])
#     dp = [0] * n
#     for i in range(m):
#         dp[0] += grid[i][0]
#         for j in range(1, n):
#             dp[j] = (min(dp[j], dp[j-1]) or dp[j-1]) + grid[i][j]
#     return dp[-1]


# grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

# print(minPathSum(grid))

def minPathSum(grid):
    rows, cols = len(grid), len(grid[0])

    res = [[float("inf")] * (cols + 1) for r in range(rows+1)]
    res[rows-1][cols] = 0
    print("res", res)
    for r in range(rows - 1, -1, -1):
        for c in range(cols-1, -1, -1):
            print(f"r {r} c {c} grid{r}{c}={grid[r][c]}")
            res[r][c] = grid[r][c] + min(res[r+1][c], res[r][c+1])

    return res[0][0]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

print(minPathSum(grid))
