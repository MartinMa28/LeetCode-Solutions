class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        nums = list(range(1, n + 1))
        fizz_buzz = [''] * n

        for index, value in enumerate(nums, 0):
            if (value % 3 == 0) and (value % 5 == 0):
                fizz_buzz[index] = 'FizzBuzz'
            elif value % 3 == 0:
                fizz_buzz[index] = 'Fizz'
            elif value % 5 == 0:
                fizz_buzz[index] = 'Buzz'
            else:
                fizz_buzz[index] = str(value)
        
        return fizz_buzz


if __name__ == "__main__":
    solu = Solution()
    print(solu.fizzBuzz(15))