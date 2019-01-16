from random import shuffle
import random

class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.org_nums = nums
        self.cur_nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.cur_nums = self.org_nums
        return self.cur_nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        self.cur_nums = sorted(self.cur_nums, key=lambda _: random.random())
        return self.cur_nums

        


# Your Solution object will be instantiated and called as such:
nums = list(range(10))
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()
print(f"param_1: {param_1}, param_2: {param_2}")
