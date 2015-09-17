import sys
import Eng

ORD = ['', 'thousand', 'million', 'billion']
low_Twenty = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
high_Twenty = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def eng_3(num):
    if num < 20:
        return low_Twenty[num]
    else:
        h = num / 10
        l = num % 10
        return high_Twenty[h-2] + ' ' + low_Twenty[l]

def eng_3(num):
    h = num / 100
    l = num % 100
    e2 = eng_2(l)
    if h == 0:  #zero condition
        return e2
    else:
        return low_Twenty[h] + ' hundred ' + e2

def eng_num(num, order):
    quotient = num / 1000
    remainder = num % 1000
    mid_res = ''
    e3 = eng_3(remainder)
    if order > 0 and not (e3 == ''):  #zero condition
        mid_res = e3 + ' ' + ORD[order]
    else:
        mid_res = e3
    if (quotient == 0):
        return mid_res
    else:
        if mid_res == '':  #zero condition
            return eng_num(quotient, order+1) + mid_res
        else:
            return eng_num(quotient, order+1) + ' ' + mid_res

def eng(num):
    return eng_num(num, 0)

if __name__ == "__main__":
    num = int(sys.argv[1])
    print eng(num)
