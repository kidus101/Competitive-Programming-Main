class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while (n >= 4):
            if (n % 4 != 0):return False
            n = n /4
        return n == 1
    
    # Time = logn'4 ---> log n in base 4
    # Space = O(1)
