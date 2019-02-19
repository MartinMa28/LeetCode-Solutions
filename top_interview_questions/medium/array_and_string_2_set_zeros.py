import numpy as np

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        is_zero = np.zeros((n_rows, n_cols))
        for i, row in enumerate(matrix):
            for j, element in enumerate(row):
                if element == 0:
                    is_zero[i, j] = 1
        
        for i in range(n_rows):
            for j in range(n_cols):
                if is_zero[i, j] == 1:
                    for t in range(n_cols):
                        matrix[i][t] = 0
                    
                    for t in range(n_rows):
                        matrix[t][j] = 0
        

if __name__ == "__main__":
    solu = Solution()
    matrix = [
        [0,1,2,0],
        [3,4,5,2],
        [1,3,1,5]
    ]
    solu.setZeroes(matrix)
    print(matrix)
