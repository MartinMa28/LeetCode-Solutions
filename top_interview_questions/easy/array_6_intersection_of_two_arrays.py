import merge_sort as sort

class Solution:
    def intersection(self, nums1, nums2):
        sorted_nums1 = sort.merge_sort(nums1)
        sorted_nums2 = sort.merge_sort(nums2)

        if sorted_nums1[0] > sorted_nums2[-1] or sorted_nums2[0] > sorted_nums1[-1]:
            return []
        
        intersection = []
        for i in sorted_nums1:
            for index_j, j in enumerate(sorted_nums2):
                if i == j:
                    intersection.append(i)
                    sorted_nums2.pop(index_j)
                    break

        return intersection
    
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1 == [] or nums2 == []:
            return []
        
        list.sort(nums1)
        list.sort(nums2)
        
        if nums1[0] > nums2[-1] or nums2[0] > nums1[-1]:
            return []
        
        intersection = []
        for i in nums1:
            for index_j, j in enumerate(nums2):
                if i == j:
                    intersection.append(i)
                    nums2.pop(index_j)
                    break

        return intersection

if __name__ == "__main__":
    solu = Solution()
    print(solu.intersect([-2147483648,1,2,3], [1,-2147483648,-2147483648]))

    