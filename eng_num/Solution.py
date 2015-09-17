class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        return self.__eng_num(num, 0)

    __ORD = ['', 'Thousand', 'Million', 'Billion']
    __low_Twenty = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    __high_Twenty = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
 
    def __eng_2(self, num):
        if num < 20:
            return self.__low_Twenty[num]
        else:
            h = num / 10
            l = num % 10
            if l == 0:  #zero condition
                return self.__high_Twenty[h-2]
            return self.__high_Twenty[h-2] + ' ' + self.__low_Twenty[l]

    def __eng_3(self, num):
        h = num / 100
        l = num % 100
        e2 = self.__eng_2(l)
        if h == 0:  #zero condition
            return e2
        else:
            if e2 == '':  #zero condition
                return self.__low_Twenty[h] + ' Hundred' + e2
            return self.__low_Twenty[h] + ' Hundred' + ' ' + e2

    def __eng_num(self, num, order):
        if (num == 0):
            return 'Zero'
        quotient = num / 1000
        remainder = num % 1000
        mid_res = ''
        e3 = self.__eng_3(remainder)
        if order > 0 and not (e3 == ''):  #zero condition
            mid_res = e3 + ' ' + self.__ORD[order]
        else:
            mid_res = e3
        if (quotient == 0):
            return mid_res
        else:
            if mid_res == '':  #zero condition
                return self.__eng_num(quotient, order+1) + mid_res
            return self.__eng_num(quotient, order+1) + ' ' + mid_res
