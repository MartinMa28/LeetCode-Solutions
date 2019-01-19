class Solution:

    @classmethod
    def __is_prime_number(cls, n):
        if not n > 1:
            return False
        else:
            for i in range(2, n):
                if n % i == 0:
                    return False
        
            return True

    def countPrimesSlow(self, n):
        """
        :type n: int
        :rtype: int
        """
        prime_counter = 0
        for i in range(n - 1, 1, -1):
            if Solution.__is_prime_number(i):
                prime_counter += 1

        return prime_counter
    

if __name__ == "__main__":
    import time
    start = time.time()
    solu = Solution()
    print(solu.countPrimesSlow(40000))
    stop = time.time()
    print('passed {} seconds'.format(stop - start))