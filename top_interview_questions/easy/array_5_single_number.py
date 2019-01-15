class Solution:
    def single_number(self, nums):
        counter = {}

        for i in nums:
            counter[i] = counter.get(i, 0) + 1
        
        for key, value in counter.items():
            if value == 1:
                return key


if __name__ == "__main__":
    solu = Solution()
    print(solu.single_number([4,1,2,1,2]))