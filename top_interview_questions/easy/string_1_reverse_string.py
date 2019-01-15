class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        length = len(s)
        tmp = ''
        for i in range(int(length/2)):
            tmp = s_list[i]
            s_list[i] = s_list[length - 1 - i]
            s_list[length - 1 - i] = tmp
        
        reversed_str = ''.join(s_list)
        return reversed_str

if __name__ == '__main__':
    solu = Solution()
    test_str = '-123'
    print(solu.reverseString(test_str))