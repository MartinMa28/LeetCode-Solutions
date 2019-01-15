import time

class Solution:
    result_table = {1: 1, 2: 2}
    # the result is equivalent to fibonacci
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.result_table.get(n, -1) == -1:
            self.result_table[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            
        return self.result_table[n]

    def heavy_fibonacci(self, n):
        heavy_table = {1: 1, 2: 2}
        if heavy_table.get(n, -1) == -1:
            heavy_table[n] = self.heavy_fibonacci(n - 1) + self.heavy_fibonacci(n - 2)
        
        return heavy_table[n]

if __name__ == "__main__":
    solu = Solution()
    start_time = time.time()
    r = solu.heavy_fibonacci(42)
    end_time = time.time()
    print(f'passed {end_time - start_time} sec, result = {r}')

        
