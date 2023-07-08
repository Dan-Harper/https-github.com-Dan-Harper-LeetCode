class Solution {
    public String minWindow(String s, String t) {
        // edge case check
        if (s == null || s.length() == 0) {
            return "";
        }

        // static array

        int[] staticArray = new int[128];

        for (char c : t.toCharArray()) {
            staticArray[c]++;
        }

        int count = 0;
        int minimumLength = Integer.MAX_VALUE;
        int minimumStart = -1;
        int minimumEnd = -1;
        int lowPointer = 0;
        int highPointer = 0;

        for (highPointer = 0; highPointer < s.length(); highPointer++) {
            if (staticArray[s.charAt(highPointer)] > 0) {
                count++;
            }

            staticArray[s.charAt(highPointer)]--;

            if (count == t.length()) {
                while (lowPointer < highPointer && staticArray[s.charAt(lowPointer)] < 0) {
                    staticArray[s.charAt(lowPointer)]++;
                    lowPointer++;
                }

                if (minimumLength > highPointer - lowPointer + 1) {
                    minimumLength = highPointer - lowPointer + 1;
                    minimumStart = lowPointer;
                    minimumEnd = highPointer + 1;
                }

                staticArray[s.charAt(lowPointer)]++;

                lowPointer++;

                count --;
            } 
        }
        return minimumStart == - 1 ? "" : s.substring(minimumStart, minimumEnd);
    }
}