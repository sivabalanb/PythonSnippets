# def searchMatrix(matrix, target):
#     j = -1
#     for row in matrix:
#         while j + len(row) and row[j] > target:
#             j -= 1
#         if row[j] == target:
#             return True
#     return False


# matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [
#     3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
# target = 14
# print(searchMatrix(matrix, target))

def searchMatrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    top, bottom = 0, rows - 1

    while top < bottom:
        row = (top+bottom) // 2
        print(f"top {top} bottom {bottom} row {row}")
        if target > matrix[row][-1]:
            bottom += 1
        elif target < matrix[row][0]:
            top -= 1
        else:
            break

    if not (top <= bottom):
        return False

    row = (top + bottom) // 2
    l, r = 0, cols - 1
    while l <= r:
        m = (l+r) // 2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True
    return False


matrix = [[1], [3]]
target = 0
print(searchMatrix(matrix, target))
