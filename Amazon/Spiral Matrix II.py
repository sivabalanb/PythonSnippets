
def generateMatrix(n):
    A = [[0] * n for _ in range(n)]
    i, j, di, dj = 0, 0, 0, 1
    for k in range(n*n):
        A[i][j] = k + 1
        print(f"A[i][j]", A[i][j])
        print(
            f" i {i} j {j} df {di} dj {dj} (j+dj) % n {(j+dj) % n} (i+di) % n {(i+di) % n}")
        if A[(i+di) % n][(j+dj) % n]:
            di, dj = dj, -di
        i += di
        j += dj
    return A


print(generateMatrix(3))
