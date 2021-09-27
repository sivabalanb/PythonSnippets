# def uniquePathsWithObstacles(OG) -> int:
#     if OG[0][0]:
#         return 0
#     m, n = len(OG), len(OG[0])
#     print(f"m {m} n {n}")
#     dp = [[0] * n for _ in range(m)]
#     dp[0][0] = 1
#     for i in range(m):
#         for j in range(n):
#             if OG[i][j] or (i == 0 and j == 0):
#                 continue
#             dp[i][j] = (dp[i-1][j] if i else 0) + (dp[i][j-1] if j else 0)
#             print(f"dp[i][j] {dp[i][j]} i {i} j {j}")
#     return dp[m-1][n-1]


# OG = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
# #OG = [[0, 1], [0, 0]]


def uniquePaths(m: int, n: int) -> int:
    row = [1] * n

    for _ in range(m-1):
        newRow = [1] * n
        for j in range(n-2, -1, -1):
            newRow[j] = newRow[j+1] + row[j]
            print(f"newRow {newRow[j]} and j {j}")
        row = newRow
        print("row", row)
    return row[0]


print(print(uniquePaths(m=7, n=3)))
