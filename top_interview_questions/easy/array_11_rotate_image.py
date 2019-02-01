class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # transpose firstly
        for i in range(1, len(matrix[0])):
            for j in range(0, i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # interchange secondly
        for i in range(int(len(matrix) / 2)):
            for j in range(len(matrix)):
                matrix[j][i], matrix[j][len(matrix) - i - 1] = matrix[j][len(matrix) - i - 1], matrix[j][i]
        

if __name__ == "__main__":
    solu = Solution()
    m = [[ 5, 1, 9,11],
        [ 2, 4, 8,10],
        [13, 3, 6, 7],
        [15,14,12,16]]
    print("before rotata: {}".format(m))
    solu.rotate(m)
    print("after rotate: {}".format(m))
    