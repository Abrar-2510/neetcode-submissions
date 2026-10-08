
# "So this problem asks if there's a root-to-leaf path where the sum equals a target value.
# Since we're dealing with paths in a tree, DFS is a natural choice because it allows us to explore one path fully until we reach a leaf.
# At each node, I subtract the node's value from the target sum, and recursively check both the left and right subtrees.
# If I reach a leaf node and the remaining sum equals the node's value, I return true.
# Otherwise, I keep exploring.
# The time complexity is O(n) since we visit each node once, and the space complexity is O(h) due to the recursion stack, where h is the height of the tree."

class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        if not root.left and not root.right:
            return targetSum == root.val
        
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))