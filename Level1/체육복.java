import java.util.*;
class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        Arrays.sort(lost);
        Arrays.sort(reserve);
        
        boolean [] able = new boolean[reserve.length];
        Arrays.fill(able, true);
        boolean[] can = new boolean[lost.length];
        
        int answer = n - lost.length;
        for(int i=0; i<lost.length; i++) {
            for(int j=0; j<reserve.length; j++) {
                if(lost[i] == reserve[j]) {
                    answer++;
                    can[i] = true;
                    able[j] = false;
                    break;
                }
            }
        }

        for(int i=0; i<lost.length; i++) {
            if(!can[i]) {
                int loster = lost[i];
                for(int j=0; j<reserve.length; j++) {
                    if(able[j]) {
                        if(loster + 1 == reserve[j] || reserve[j] == loster-1) {
                            able[j] = false;
                            answer++;
                            break;
                        }
                    }
                }
            }
        }
        
        return answer;
    }
}
