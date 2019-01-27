class Solution():
    def reverseBits(self, n):
        bits_len = 32
        reversed_int = 0
        for i in range(bits_len):
            lsb = n & 1
            reversed_int |= lsb
            if i == 31:
                break
            reversed_int = reversed_int << 1
            n = n >> 1
        
        return reversed_int


if __name__ == "__main__":
    solu = Solution()
    print(solu.reverseBits(-3))