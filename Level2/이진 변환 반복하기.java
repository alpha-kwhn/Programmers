import java.util.*;

class Solution {
    public String change(int num) {
        StringBuilder sb = new StringBuilder();
        while(num > 0) {
            sb.append(num % 2);
            num /= 2;
        }
        return sb.reverse().toString();
    }
    
    public int[] solution(String s) {
        int[] answer = new int[2];
        String k = s;
        while(!k.equals("1")) {
            int size = k.length();
            String tmp = k.replace("0", "");
            answer[1] += size - tmp.length();
            
            int num = Integer.valueOf(tmp.length());
            k = change(num);
            answer[0]++;
        }
        return answer;
    }
}
