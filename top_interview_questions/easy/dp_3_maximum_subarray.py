class Solution:

    def max_subarray(self, nums):
        result = 0
        current = 0
        for i in nums:
            current = current + i
            result = max(result, current)
            current = max(0, current)
        
        return result


if __name__ == "__main__":
    solu = Solution()

    print(solu.max_subarray([-2,1,-3,4,-1,2,1,-5,4]))