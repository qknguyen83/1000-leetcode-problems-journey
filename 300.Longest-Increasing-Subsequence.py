class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        theList = [1]
        
        for i in range(1, len(nums)):
            maxi = 0
            for j in range(len(theList) - 1, -1, -1):
                if nums[j] < nums[i] and theList[j] > maxi:
                    maxi = theList[j]
            theList.append(maxi + 1)
            
        return max(theList)
