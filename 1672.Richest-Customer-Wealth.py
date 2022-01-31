class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for account in accounts:
            wealth = sum(account)
            if maxWealth < wealth:
                maxWealth = wealth
                
        return maxWealth
