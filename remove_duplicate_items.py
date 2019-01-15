class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while(i < len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
            else:
                i += 1
        
        return len(nums)
        
nums = [0,0,1,1,1,2,2,3,3,4]
Solu = Solution()
rem_len = Solu.removeDuplicates(nums)
print(nums)
print(rem_len)