class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) >= 3 and arr[0] < arr[1]:
            switch = 1
            for i in range(1, len(arr)):
                if switch == 1:
                    if arr[i] < arr[i-1]:
                        switch = -1
                    elif arr[i] == arr[i-1]:
                        break
                else:
                    if arr[i] >= arr[i-1]:
                        break
                
                if i == len(arr) - 1 and switch == -1:
                    return True
                
        return False
