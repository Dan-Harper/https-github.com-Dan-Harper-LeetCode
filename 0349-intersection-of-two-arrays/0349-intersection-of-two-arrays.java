class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        HashSet<Integer> setTrack = new HashSet<Integer>();
        // setTrack for numbers seen in nums1
        for(int i : nums1) {
            setTrack.add(i);
        }
        // hashset for intersection of num arrays
        HashSet<Integer> setIntersection = new HashSet<Integer>();
        for(int i : nums2) {
            if(setTrack.contains(i)) {
                setIntersection.add(i);
            }
        }
        // result return num array
        int[] result = new int [setIntersection.size()];
        int index = 0;
        for(int i : setIntersection) {
            result[index++] = i;
        }
        return result;
    }
}