class Solution():
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        
        memo = [0] * (len(nums) + 1)
        # 2 probabilities: 1) rob the first house 2) don't rob the first house
        memo[0] = 0
        memo[1] = nums[0]

        for i in range(1, len(nums)):
            memo[i + 1] = max(memo[i], memo[i - 1] + nums[i])
        
        return memo[-1]

if __name__ == "__main__":
    solu = Solution()
    print(solu.rob([1,2,3,1]))