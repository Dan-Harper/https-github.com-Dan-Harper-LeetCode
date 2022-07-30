class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<Integer>();
        for(int index : nums){
            if(set.contains(index)) {
                return true;
            } else {
                set.add(index);
            }
        }
        return false;
    }
}