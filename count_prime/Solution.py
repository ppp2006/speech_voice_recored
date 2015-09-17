from math import *
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        pl = range(2, n)
        cursor = 0
        while cursor < len(pl):
            p = pl[cursor]
            if self.__is_prime(p):
                for i in pl[(cursor+1):]:
                    if i % p == 0:
                        pl.remove()
            cursor = cursor +1
        return cursor

    def __is_prime(self, num):
        mid = floor(sqrt(num))
        loop = 2
        while loop <= mid:
            if num % loop == 0:
                return False
            loop = loop +1
        return True
