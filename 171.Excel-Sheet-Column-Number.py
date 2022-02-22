class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        length = len(columnTitle)
        ans = 0
        for i in range(0, length):
            ans = ans + (ord(columnTitle[i]) - 64) * pow(26, length - i - 1)
            
        return ans
