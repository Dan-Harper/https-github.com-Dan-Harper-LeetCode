class Solution {
    public boolean judgeCircle(String moves) {
        int x = 0;
        int y = 0;
        for(int i = 0; i < moves.length(); i++) {
            char character = moves.charAt(i);
            if(character == 'R') {
                x += 1;
            } else if(character == 'L'){
                x -= 1;
            } else if (character == 'U') {
                y += 1;
            } else if (character == 'D') {
                y -= 1;
            }
        }
        if(x == 0 && y == 0) {
            return true;
        } else {
            return false;
        }
    }
}