class Solution:
    def helper(self, coins, amount):
        if amount in self.theDict:
            return self.theDict[amount]
        
        if amount < 0:
            return -1
        elif amount == 0:
            return 0
        else:
            maxi = -10000
            mini = 10000
            for coin in coins:
                temp = self.helper(coins, amount - coin)
                if maxi < temp:
                    maxi = temp
                if mini > temp and temp >= 0:
                    mini = temp
            if maxi == -1:
                self.theDict[amount] = -1
            else:
                self.theDict[amount] = 1 + mini
            return self.theDict[amount]
            
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.theDict = dict()
        return self.helper(coins, amount)
