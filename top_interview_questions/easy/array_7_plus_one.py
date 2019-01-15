class Solution:
    def plus_one(self, nums):
        if nums == []:
            return [1]
        if nums[-1] != 9:
            nums[-1] += 1
            return nums
        else:
            return self.plus_one(nums[:-1]) + [0]

if __name__ == "__main__":
    solu = Solution()
    print(solu.plus_one([9,9]))