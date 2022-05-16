class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        tempResult = 0
        for i in range(0, len(nums)):
            tempResult = max(nums[i] + tempResult, nums[i])
            result = max(result, tempResult)
        return result
