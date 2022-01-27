class Solution:
    def helper(self, root, arr):
        if root != None:
            self.helper(root.left, arr)
            self.helper(root.right, arr)
            arr.append(root.val)
            
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.helper(root, arr)
        
        return arr
