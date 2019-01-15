class Solution:
    def move_zeroes(self, nums):
        index = 0
        while index < len(nums):
            if nums[index] == 0:
                if nums[index:] == [0] * len(nums[index:]):
                    break
                nums.insert(len(nums), nums.pop(index))
            else:
                index += 1



if __name__ == "__main__":
    solu = Solution()
    test = [0,0,3]
    solu.move_zeroes(test)
    print(test)
