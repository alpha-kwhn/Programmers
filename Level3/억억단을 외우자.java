import java.util.*;

class Solution {
    public int[] solution(int e, int[] starts) {
        int [] dic = new int[e+1];
        for(int i=1; i<=e; i++) {
            for(int j=1; j<=e; j++) {
                if(i*j <= e) dic[i*j] += 1;
                else break;
            }
        }
        
        int mini = Integer.MAX_VALUE;
        for(int i=0; i<starts.length; i++) 
            mini = Math.min(mini, starts[i]);
        
        int [] answer = new int[e+1];
        int maxi = 0;
        
        for(int i=e; i>=mini; i--) {
            if(i == e) {
                answer[e] = e;
                maxi = e;
            } else {
                if(dic[i] >= dic[maxi]) {
                    maxi = i;
                    answer[i] = i;
                } else 
                    answer[i] = maxi;
            }
        }
        
        int [] result = new int[starts.length];
        for(int i=0; i<starts.length; i++) 
            result[i] = answer[starts[i]];
        
        return result;
    }
}
