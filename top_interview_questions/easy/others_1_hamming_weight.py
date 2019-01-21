# Review of Python Bitwise Operation
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        hamming_weight = 0
        while n > 0:
            # computes the bitwise AND on n and 1, which tests whether
            # n's least significant bit is 1
            # adds 1 to the hamming weight, if current bit is one
            # adds 0 otherwise
            hamming_weight += (n & 1)
            # right shift 1 bit
            n = n >> 1
        
        return hamming_weight

if __name__ == "__main__":
    solu = Solution()
    print(solu.hammingWeight(5))