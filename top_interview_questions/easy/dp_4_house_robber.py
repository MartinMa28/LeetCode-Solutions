class Solution():
    def find_max_index(nums):
        max_value = -1
        max_index = 0
        for index, value in enumerate(nums, 0):
            if value > max_value:
                max_value = value
                max_index = index
        
        return max_index
                

    def rob(self, nums):
        pass


if __name__ == "__main__":
    solu = Solution()
    print(solu.rob([2,7,9,3,1]))
    
    print(sum([2,7,9,3,1]))

        