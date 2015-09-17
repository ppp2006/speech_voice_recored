class Solution(object):
    __prime_list = [2]
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 2
        while num <= n:
            if self.__is_prime(num):
                self.__prime_list.append(num)
            num = num +1
        return len(self.__prime_list)

    def __find_mid(self, num):
        num_digits = 1;
        while num >> num_digits != 0:
            num_digits = num_digits +1
        return 2 ** ((num_digits+1)/2)

    def __is_prime(self, num):
        mid = self.__find_mid(num)
        for i in self.__prime_list:
            if num % i == 0:
                return False
            if i > mid:
                break
        loop = self.__prime_list[-1] +1
        while loop <= mid:
            if num % loop == 0:
                return False
            loop = loop +1
        return True
