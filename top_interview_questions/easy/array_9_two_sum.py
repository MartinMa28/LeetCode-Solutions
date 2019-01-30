class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_indices = sorted(range(len(nums)), key=lambda ind: nums[ind])
        for ind_of_ind, ind1 in enumerate(sorted_indices[:-1]):
            num1 = nums[ind1]
            temp_sum = num1
            for ind2 in sorted_indices[:ind_of_ind] + sorted_indices[ind_of_ind + 1:]:
                num2 = nums[ind2]
                temp_sum += num2
                if temp_sum < target:
                    temp_sum -= num2
                elif temp_sum == target:
                    return [ind1, ind2]

if __name__ == "__main__":
    solu = Solution()
    print(solu.twoSum([3,2,3], 6))