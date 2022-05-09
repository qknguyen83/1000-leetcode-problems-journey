class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = nums[0]
        theList = [nums[0], nums[0]]
        for i in range(1, len(nums)):
            tempList = [nums[i], nums[i] * theList[0], nums[i] * theList[1]]
            theList = [max(tempList), min(tempList)]
            if maxi < theList[0]:
                maxi = theList[0]
        return maxi
