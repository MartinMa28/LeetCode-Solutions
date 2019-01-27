class Solution():
    def isPalindrome(self, s):
        import re
        matches = re.findall('[0-9A-Za-z]', s)
        lower = [ch.lower() for ch in matches]
        half_lenth = int(len(lower) / 2)

        for i in range(half_lenth):
            if lower[i] != lower[-i - 1]:
                return False
        
        return True
