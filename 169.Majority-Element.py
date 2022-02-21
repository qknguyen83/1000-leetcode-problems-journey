class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        theDict = dict()
        for num in nums:
            if num not in theDict:
                theDict[num] = 0
            theDict[num] = theDict[num] + 1
            if theDict[num] > len(nums) / 2:
                return num
