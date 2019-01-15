class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_char = {}
        length = len(s)
        for i in range(length):
            if dict_char.get(s[i], 0) < 2:
                dict_char[s[i]] = dict_char.get(s[i], 0) + 1
        
        for i in range(length):
            if dict_char[s[i]] == 1:
                return i
        
        return -1

if __name__ == "__main__":
    solu = Solution()
    print(solu.firstUniqChar('leetcode'))
