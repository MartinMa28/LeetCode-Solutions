class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        elif n == 1:
            return True
        elif n % 3 == 0:
            return self.isPowerOfThree(n / 3)
        else:
            return False


if __name__ == "__main__":
    solu = Solution()
    print(solu.isPowerOfThree(45))