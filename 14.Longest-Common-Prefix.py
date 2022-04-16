class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        
        for i in range(1, len(strs)):
            minLen = len(ans) if len(ans) <= len(strs[i]) else len(strs[i])
            
            temp = ''
            for j in range(0, minLen):
                if ans[j] == strs[i][j]:
                    temp = temp + ans[j]
                else:
                    break
            
            ans = temp
            
        return ans
