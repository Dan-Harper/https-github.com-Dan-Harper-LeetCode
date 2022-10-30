/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        // error checking
        if(nums == null || nums.length == 0) {
            return null;
        }
        // call recursive function
        // 0 = left pointer
        // nums.length - 1 = right pointer
        return constructBTSRecursive(nums, 0, nums.length - 1);
    }
    
    private TreeNode constructBTSRecursive(int[] nums, int left, int right) {
        // if tree leaf
        if(left > right) {
            return null;
        }
        int mid = left + (right - left) / 2;
        // construct class
        TreeNode current = new TreeNode(nums[mid]);
        current.left = constructBTSRecursive(nums, left, mid - 1);
        current.right = constructBTSRecursive(nums, mid + 1, right);
        return current;
    }
}