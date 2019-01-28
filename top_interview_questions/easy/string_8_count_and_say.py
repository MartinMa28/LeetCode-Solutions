class Solution():
    
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def count(s):
            if s == '1':
                return '11'
            else:
                next_str = ''
                counter = 1
                last_bit = s[0]
                for i in range(1, len(s)):
                    if s[i] == last_bit:
                        counter += 1
                    else:
                        next_str += str(counter) + last_bit
                        last_bit = s[i]
                        counter = 1
                    
                    if i == len(s) - 1:
                        next_str += str(counter) + last_bit
                        return next_str
                
        
        val = '1'
        for i in range(n - 1):
            val = count(val)
        
        return val

if __name__ == "__main__":
    solu = Solution()
    print(solu.countAndSay(4))