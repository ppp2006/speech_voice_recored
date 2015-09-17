#include <stdint.h>
#include <iostream>
#include <cmath>
class Solution {

public:

    int countPrimes(int n) {
        uint32_t counts = 0;
        for (uint32_t i = 2; i < n; i++) {
            
        }
    }

    bool isPrime(n) {
        uint32_t mid = floor(sqrt(n));
        for (uint32_t i = 2; i < mid; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

};

int main(){
    s = Solution();

}
