
def generateMatrix(n):
    # A = [[0] * n for _ in range(n)]
    # i, j, di, dj = 0, 0, 0, 1
    # for k in range(n*n):
    #     A[i][j] = k + 1
    #     print(f"A[i][j]", A[i][j])
    #     print(
    #         f" i {i} j {j} df {di} dj {dj} (j+dj) % n {(j+dj) % n} (i+di) % n {(i+di) % n}")
    #     if A[(i+di) % n][(j+dj) % n]:
    #         di, dj = dj, -di
    #     i += di
    #     j += dj
    # return A
    res = []
    top, bottom = 0, len(n)
    left, right = 0, len(n[0])

    while top < bottom and left < right:
        # get value in top row
        for i in range(left, right):
            res.append(n[top][i])
        top += 1

        # get value from top to bottom - right
        for i in range(top, bottom):
            res.append(n[i][right - 1])
        right -= 1

        # get value from right to left - bottom
        for i in range(right-1, left-1):
            res.append(n[bottom-1][i])
        bottom -= 1

        # get value from bottom to top - left
        for i in range(bottom-1, top - 1):
            res.append(n[i][left])
        left += 1

    return res


print(generateMatrix(3))
