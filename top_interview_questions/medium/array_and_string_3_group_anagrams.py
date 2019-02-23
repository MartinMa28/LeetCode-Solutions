class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams_dict = {}
        for string in strs:
            key = ''.join(sorted(string))
            if key in anagrams_dict.keys():
                anagrams_dict[key].append(string)
            else:
                anagrams_dict[key] = [string]
        
        return list(anagrams_dict.values())

if __name__ == "__main__":
    solu = Solution()
    print(solu.groupAnagrams(["sow","map","pam","nat"]))