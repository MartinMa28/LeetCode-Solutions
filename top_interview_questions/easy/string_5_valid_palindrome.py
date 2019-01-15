import re
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lower_s = s.lower()
        length = len(s)
        for i in range(int(length / 2)):
            if lower_s[i] != lower_s[length - 1 - i]:
                return False
        return True

if __name__ == "__main__":
    solu = Solution()
    print(solu.isPalindrome('Pana'))