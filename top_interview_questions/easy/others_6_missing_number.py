class Solution():
    def missing_number(self, nums):
        included_miss = sum(range(1, len(nums) + 1))
        total = sum(nums)
        return included_miss - total