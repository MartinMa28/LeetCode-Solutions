class Solution:
    roman = {'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000}

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        int_val = 0
        for index, ch in enumerate(s):
            if index < len(s) - 1:
                # there is a following character, which could be greater than current one
                if self.roman[ch] < self.roman[s[index + 1]]:
                    # subtract current value from the following value
                    int_val -= self.roman[ch]
                else:
                    int_val += self.roman[ch]
            else:
                # current character is the last one
                int_val += self.roman[ch]

        return int_val

if __name__ == "__main__":
    solu = Solution()
    print(solu.romanToInt("MCMXCIV"))