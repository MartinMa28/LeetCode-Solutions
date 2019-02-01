class Solution():
    def __init__(self):
        self.memo = []
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.memo = [0] * len(nums)
        return self.__rob(nums, len(nums) - 1)

    def __rob(self, nums, i):
        if i < 0:
            return 0
        elif self.memo[i] > 0:
            return self.memo[i]
        else:
            self.memo[i] = max(self.__rob(nums, i - 2) + nums[i], self.__rob(nums, i - 1))
            return self.memo[i]


if __name__ == "__main__":
    solu = Solution()
    print(solu.rob([1, 2, 3, 1]))
        