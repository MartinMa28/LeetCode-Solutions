# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# dummy function for linter
def isBadVersion(n):
    if n < 4:
        return False
    return True

class Solution(object):
    
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        
        def bi_search(cur):
            nonlocal left
            nonlocal right
            if left == right:
                return left
            elif isBadVersion(cur):
                right = cur
                return bi_search(int((left + right) / 2))
            else:
                left = cur + 1
                return bi_search(int((left + right) / 2))
        
        return bi_search(int((left + right)/2))


if __name__ == "__main__":
    solu = Solution()
    print(solu.firstBadVersion(5))