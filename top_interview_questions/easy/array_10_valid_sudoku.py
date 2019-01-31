import numpy as np

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def test_repetition(nums):
            container = []
            for ele in nums:
                if ele in container and ele != '.':
                    return True
                if ele != '.':
                    container.append(ele)
            
            return False

        # test row-wise
        for row in board:
            if test_repetition(row):
                return False

        # test column-wise
        for i in range(len(board[0])):
            if test_repetition([row[i] for row in board]):
                return False
        
        
        # test 3x3 sub-box-wise
        np_board = np.array(board)
        
        for i in range(3):
            for j in range(3):
                sub_box = np_board[i * 3:i * 3 + 3, j * 3:j * 3 + 3].flatten()
                if test_repetition(sub_box):
                    return False

        return True

if __name__ == "__main__":
    solu = Solution()
    print(solu.isValidSudoku([
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
    ]))
    
