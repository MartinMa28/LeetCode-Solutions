class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        def reverseString(s):
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
        
        upper_bound = 2 ** 31 - 1
        lower_bound = -(2 ** 31)
        negative = (x < 0)
        if negative:
            x = -x
        reversed_str = reverseString(str(x))
        reversed_int = int(reversed_str)
        
        if negative:
            result = -(reversed_int)
        else:
            result = reversed_int

        if result < lower_bound or result > upper_bound:
            return 0
        else:
            return result

if __name__ == "__main__":
    solu = Solution()
    test = -123
    print(solu.reverse(test))