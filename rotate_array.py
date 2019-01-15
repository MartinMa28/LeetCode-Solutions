class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
           right_most = nums.pop()
           nums.insert(0,right_most) 
        

a = [-1,-100,3,99]
k = 2
Solu = Solution()
Solu.rotate(a,k)
print(a)