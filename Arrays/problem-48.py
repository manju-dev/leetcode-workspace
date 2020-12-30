# 48. Rotate Image
class Solution:
    # Approach 1
    def rotate1(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix.reverse()
        # swap symmetry
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Approach 2
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # swap symmetry
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reverse side by side
        for row in matrix:
            for j in range(n//2):
                row[j], row[~j] = row[~j], row[j]
# Test
solution = Solution()
# Expected: 90 degree rotation
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
solution.rotate(matrix)
print(matrix)