class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        insert_at = 0
        while len(nums2) != 0:
            temp = nums2.pop(0)
            while insert_at < len(nums1) and temp >= nums1[insert_at]:
                insert_at += 1
            nums1.insert(insert_at, temp)

if __name__ == "__main__":
    n1 = [1, 3, 6, 7]
    n2 = [1, 2, 4, 4, 5, 9]
    solu = Solution()
    solu.merge(n1, len(n1), n2, len(n2))
    print(n1)
            
