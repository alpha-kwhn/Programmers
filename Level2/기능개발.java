import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> stack = new ArrayList<>();
        ArrayList<Integer> answer = new ArrayList<>();
        for(int i=0; i<speeds.length; i++) {
            int days = (int)(100 - progresses[i]) / speeds[i];
            int last = (100 - progresses[i]) % speeds[i];
            if(last > 0) 
                ++days;
            stack.add(days);
        }
        
        int cnt = 1;
        int cur = stack.get(0);
        
        for(int i=1; i<stack.size(); i++) {
            if(cur < stack.get(i)) {
                answer.add(cnt);
                cnt = 1;
                cur = stack.get(i);
            } else 
                cnt++;
        }
        answer.add(cnt);
        
        
        int [] result = new int[answer.size()];
        for(int i=0; i<answer.size(); i++)
            result[i] = answer.get(i);
        return result;
    }
}
