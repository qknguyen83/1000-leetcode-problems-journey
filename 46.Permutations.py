class Solution:
    def helper(self, nums, n, record, entry, result):
        if n == 1:
            for i in range(0, len(nums)):
                if i not in record:
                    entry.append(nums[i])
                    result.append(entry.copy())
                    del entry[-1]
        else:
            for i in range(0, len(nums)):
                if i not in record:
                    record.append(i)
                    entry.append(nums[i])
                    self.helper(nums, n - 1, record, entry, result)
                    del record[-1]
                    del entry[-1]
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.helper(nums, len(nums), [], [], result)
        return result
