class Solution:
    def countVowelStrings(self, n: int) -> int:
        theList = [1, 1, 1, 1, 1]
        result = 5
        
        for i in range(1, n):
            newList = [result]
            for j in range(1, 5):
                newList.append(newList[j-1] - theList[j-1])
            theList = newList
            result = sum(theList)
            
        return result
