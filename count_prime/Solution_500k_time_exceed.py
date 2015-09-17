from math import *
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        counts = 0
        num = 2
        while num <= n:
            if self.__is_prime(num):
                counts = counts + 1
            num = num +1
        return counts

    def __is_prime(self, num):
        mid = floor(sqrt(num))
        loop = 2
        while loop <= mid:
            if num % loop == 0:
                return False
            loop = loop +1
        return True
