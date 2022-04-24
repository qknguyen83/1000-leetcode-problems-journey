class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        record = list()
        record.append(cost[0])
        record.append(cost[1])
        
        ans = min(record[0], record[1])
        for i in range(2, len(cost)):
            newRecord = cost[i] + ans
            record.append(newRecord)
            ans = min(record[len(record) - 1], record[len(record) - 2])
            
        return ans
