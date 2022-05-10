class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        theDict = dict()
        for index, value in enumerate(nums):
            if theDict.get(value) != None:
                return [theDict[value], index]
            theDict[target - value] = index
