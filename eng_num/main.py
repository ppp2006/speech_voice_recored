import sys
import Solution

if __name__ == "__main__":
    num = int(sys.argv[1])
    sol = Solution.Solution()
    print sol.numberToWords(num)
