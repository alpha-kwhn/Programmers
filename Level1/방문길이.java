import java.util.*;

class Solution {
    public int solution(String dirs) {
        int x = 0;
        int y = 0;
        int answer = 0;
        
        HashSet<String> sets = new HashSet<>();
        
        char [] arr = dirs.toCharArray();
        
        for(Character c : arr) {
            boolean able = true;
            int first_x = x;
            int first_y = y;
            
            if(c == 'U' && y+1 <= 5)
                y++;
            else if(c == 'D' && y-1 >= -5)
                y--;
            else if(c == 'R' && x+1 <= 5)
                x++;
            else if(c == 'L' && x-1 >= -5)
                x--;
            else
                able = false;
            
            if(able) {
                sets.add(first_x + ", " + first_y + ", " + x + ", " + y);
                sets.add(x + ", " + y + ", " + first_x + ", " + first_y);
            }
        }
        
        return sets.size() / 2;
    }
}
