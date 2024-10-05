import java.util.*;

class Solution {
    public int[] solution(int brown, int yellow) {
        int size = brown + yellow;
        int[] answer = new int[2];
        for(int i=1; i<=size; i++) {
            if(size % i > 0)
                continue;
            else {
                int col = (size / i);
                if(((i*2) + ((col-2)*2) == brown) && ((i-2)*(col-2) == yellow)) {
                    answer[0] = Math.max(i, col);
                    answer[1] = Math.min(i, col);
                    break;
                }
            }
        }
        return answer;
    }
}
