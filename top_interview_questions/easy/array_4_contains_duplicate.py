class Solution:
    def contains_duplicate(self, nums):
        return not len(set(nums)) == len(nums)