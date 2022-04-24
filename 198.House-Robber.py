class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        record = list()
        record.append(nums[0])
        record.append(max(nums[0], nums[1]))
        
        for i in range(2, len(nums)):
            newRecord = max(nums[i] + record[len(record) - 2], record[len(record) - 1])
            record.append(newRecord)
            
        return record[len(record) - 1]
