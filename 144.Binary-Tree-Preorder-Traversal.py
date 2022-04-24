class Solution:
    def helper(self, root, arr):
        if root != None:
            arr.append(root.val)
            self.helper(root.left, arr)
            self.helper(root.right, arr)
            
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.helper(root, arr)
        
        return arr
