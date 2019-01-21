class Solution():
    def hammingDistance(self, x, y):
        xor = x ^ y
        distance = 0
        while xor > 0:
            distance += xor & 1
            xor = xor >> 1
        
        return distance

if __name__ == "__main__":
    solu = Solution()
    print(solu.hammingDistance(1, 4))