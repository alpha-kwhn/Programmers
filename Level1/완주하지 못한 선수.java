import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> marathon = new HashMap<>();
        for(String par : participant) 
            marathon.put(par, 0);
        for(String fin : participant) {
            int tmp = marathon.get(fin);
            marathon.put(fin, tmp+1);
        }
        
        String answer = "";
        for(String fin : completion) {
            int tmp = marathon.get(fin);
            marathon.put(fin, tmp-1);
        }
        
        ArrayList<String> keys = new ArrayList<>(marathon.keySet());
        for(String key : keys) {
            int tmp = marathon.get(key);
            if(tmp > 0) {
                answer = key;
                break;
            }   
        }
        
        return answer;
    }
}
