def searchMatrix(matrix, target):
    j = -1
    for row in matrix:
        while j + len(row) and row[j] > target:
            j -= 1
        if row[j] == target:
            return True
    return False


matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [
    3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 14
print(searchMatrix(matrix, target))
