class Solution():
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        lcp = ''
        for i in range(min([len(s) for s in strs])):
            cur_char = strs[0][i]
            for s in strs:
                if s[i] != cur_char:
                    return lcp
            lcp += cur_char
        
        return lcp


if __name__ == "__main__":
    solu = Solution()
    print(solu.longestCommonPrefix(["dog","racecar","car"]))
