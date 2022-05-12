class Solution:
    def helper(self, nums, n, record, entry, resultSet):
        if n == 1:
            for i in range(0, len(nums)):
                if i not in record:
                    entry.append(nums[i])
                    resultSet.add(tuple(entry))
                    del entry[-1]
        else:
            for i in range(0, len(nums)):
                if i not in record:
                    record.append(i)
                    entry.append(nums[i])
                    self.helper(nums, n - 1, record, entry, resultSet)
                    del record[-1]
                    del entry[-1]
                    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        resultSet = set()
        self.helper(nums, len(nums), [], [], resultSet)
        
        resultList = []
        for i in resultSet:
            resultList.append(list(i))
        
        return resultList
