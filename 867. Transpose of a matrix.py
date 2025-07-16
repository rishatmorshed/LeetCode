def transposeMatrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    newMat = [[0]*m for i in range(n)]
    for i in range(m):
        for j in range(n):			# Time Complexity O(n*m)
            newMat[j][i] = matrix[i][j]		# Space Complexity O(m*n)
    return newMat