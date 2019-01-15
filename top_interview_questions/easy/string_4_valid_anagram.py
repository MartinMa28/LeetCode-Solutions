class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        def generate_bash_table(s):
            h_t = {}
            for i in range(len(s)):
                h_t[s[i]] = h_t.get(s[i], 0) + 1
            
            return h_t
        
        s_set = set(s)
        t_set = set(t)
        if s_set != t_set:
            return False

        s_hash = generate_bash_table(s)
        t_hash = generate_bash_table(t)

        for ch in s_set:
            if s_hash[ch] != t_hash[ch]:
                return False
        
        return True

if __name__ == "__main__":
    
    solu = Solution()
    print(solu.isAnagram('rat', 'cat'))
