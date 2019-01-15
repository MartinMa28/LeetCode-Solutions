import concurrent.futures
import math
import time
import dp_1_climb_stairs as dp

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    args = [38, 39, 40]
    solu = dp.Solution()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        # for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
        #     print('%d is prime: %s' % (number, prime))
        for num, fibo in zip(args, executor.map(solu.heavy_fibonacci, args)):
            print(f"{num}'s fibonacci sequence: {fibo}")

def heavy_main():
    args = [38, 39, 40]
    solu = dp.Solution()
    for num, fibo in zip(args, map(solu.heavy_fibonacci, args)):
        print(f"{num}'s fibonacci sequence: {fibo}")

if __name__ == '__main__':
    start_time = time.time()
    heavy_main()
    stop_time = time.time()
    print(f"passed {stop_time - start_time}")