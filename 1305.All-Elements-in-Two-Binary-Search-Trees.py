class Solution:
    def inOrder(self, root, arr):
        if root != None:
            self.inOrder(root.left, arr)
            arr.append(root.val)
            self.inOrder(root.right, arr)
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        arr1 = []
        arr2 = []
        
        self.inOrder(root1, arr1)
        self.inOrder(root2, arr2)
        
        arr = []
        while arr1 and arr2:
            if arr1[0] < arr2[0]:
                arr.append(arr1[0])
                arr1 = arr1[1:]
            else:
                arr.append(arr2[0])
                arr2 = arr2[1:]
        
        return arr + arr1 + arr2
