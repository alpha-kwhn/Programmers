import java.util.*;

class Solution {
    public int yaksu(int num) {
        int answer = 1;
        if(num == 1)
            return 0;
        else {
            for(int i=2; i<=Math.sqrt(num); i++) {
                if(num % i == 0) {
                    answer = i;
                    if(num / i <= 10_000_000)
                        return (int)(num / i);
                }
            }
            return answer;
        }
    }
    
    public int[] solution(long begin, long end) {
        int [] answer = new int[(int)(end-begin)+1];
        int idx = 0;
        for(int i=(int)begin; i<=end; i++) 
            answer[idx++] = yaksu(i);
        
        return answer;
    }
}
