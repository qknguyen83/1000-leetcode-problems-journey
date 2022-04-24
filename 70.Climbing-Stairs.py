class Solution:
    def climbStairs(self, n: int) -> int:
        minusOne = 2
        minusTwo = 1
        
        if n == 1:
            return minusTwo
        elif n == 2:
            return minusOne
        
        while n > 2:
            current = minusOne + minusTwo
            minusTwo = minusOne
            minusOne = current
            n = n - 1
            
        return minusOne
